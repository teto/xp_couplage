

#include <linux/genetlink.h>
#include <linux/inet.h>
#include <net/genetlink.h>
// #include <net/core/utils.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <net/mptcp.h>
#include "lig_module.h"

// For tests only
#include <linux/hrtimer.h>

#define MAX_STRING     16
#define MAX_TAB        16
#define TIMER_DELAY 20000

#define lig_debug(fmt, args...)                   \
    do {                                \
            trace_printk( __FILE__ ": " fmt, ##args ); \
    } while (0);


//static int entier;
// static char destinationIP[MAX_STRING];

// TODO retrieve it automatically ?
// by default my attributed EID
static char hostEID[INET_ADDRSTRLEN] = "153.16.49.112";
// static char resolverEID[INET_ADDRSTRLEN] = "153.16.49.112";

//! Path towards the lig program
//static char programPath[100];

static struct genl_multicast_group lig_multicast_group =
{
    .name = LIG_GROUP_NAME
};


static struct timer_list my_timer;


// u8
static u32 number_of_local_rlocs = 1;

// sock
//static struct sock *nl_sk = NULL;

// module_param_string(destinationIP, destinationIP, sizeof(destinationIP), 0644);
// module_param_string(programPath, programPath, sizeof(programPath), 0644);

// MODULE_PARM_DESC(resolverEID, "EID of the (proxy) map resolver");
// MODULE_PARM_DESC(hostEID, "EID of the running machine");
// MODULE_PARM_DESC(programPath, "Path towards the userspace lig program this module calls ?");



MODULE_DESCRIPTION("lig_module");
MODULE_AUTHOR("Matthieu Coudron");
MODULE_LICENSE("GPL");


/** callback triggered on netlink message **/
int handle_results(struct sk_buff *skb_2, struct genl_info *info);



/* family definition */
static struct genl_family lig_gnl_family = {
	.id = GENL_ID_GENERATE,         /* genetlink should generate an id */
	.hdrsize = LIG_GENL_HDRLEN,
	.name = LIG_FAMILY_NAME,        /*the name of this family, used by userspace application */
	.version = LIG_GENL_VERSION,                   //version number
	.maxattr = ELA_MAX    /* a changer? ARRAY_SIZE */
};




/*
commands: mapping between the command enumeration and the actual function
genlmsg_reply(
*/
struct genl_ops lig_genl_ops[ELC_MAX] = {

    {
        .cmd = ELC_REQUEST_RLOCS_FOR_EID,
        //.flags = 0,
        .policy = lig_policies,
        .doit = handle_results /* cb function should set this one or next but not both */
        //.dumpit = NULL,               /* cb function */
        // .done        /* once dump finished */

    } ,
    {
        .cmd = ELC_RESULTS,
        .policy = lig_policies,
        .doit = handle_results /* cb function */

    },
    {
        .cmd = ELC_SET_MAP_RESOLVER,
        .policy = lig_policies,
        .doit = handle_results /* cb function */

    }
};


/** returns string associated to that command **/
// static char* getCommandStr(lig_command_t cmd)
static char* getCommandStr(E_LIG_COMMAND cmd)
{
    // if(cmd == ELC_MAX)
    // {


    // }
    return commandsStr[cmd];
}

// static char* getAttributeStr(E_LIG_ATTRIBUTE attr)
// {
//     return attributesStr[attr];
// }


/**
send the request
NLM_F_ECHO
struct genl_info *info
**/
int send_request_for_eid(u32 eid, u32 token)
{
    //!
    struct sk_buff *skb = 0;
    int rc = 0;
    void *msg_head;
    // char strEID[INET_ADDRSTRLEN] = "";

    // snprintf(strEID,"%u.%u.%u.%u", NIPQUAD(eid) );
    // nto


    // printk( "sending request for eid\n " );
    lig_debug( "sending request to userspace for eid %u.%u.%u.%u and token %#x \n", NIPQUAD(eid), token );


    /* send a message back*/
    /* allocate some memory, since the size is not yet known use NLMSG_GOODSIZE
    GPF kernel take smore time but more chance to get memory
    */
    skb = genlmsg_new(NLMSG_GOODSIZE, GFP_KERNEL);

    if (skb == NULL)
    {
        lig_debug(KERN_ERR "could not allocate space for new msg");
        return -ENOMEM;
    }
    /* create the message headers
         arguments of genlmsg_put:
           struct sk_buff *,
           int (sending) pid,
           int sequence number,
           struct genl_family *,
           int flags,
           u8 command index (why do we need this?)
*/

 // TODO passer des NL_AUTO plutot ?
    msg_head = genlmsg_put(
                        skb,
                        0,            /* no de port  */
                        0, /* no de seq (NL_AUTO_SEQ ne marche pas) */
                        &lig_gnl_family,
                        LIG_GENL_HDRLEN,    /* header length (to check) */
                        ELC_REQUEST_RLOCS_FOR_EID   /* command */
                        );

    if (msg_head == NULL) {
        lig_debug( KERN_ERR "could not create generic header\n");

        return -ENOMEM;

    }

    /* puts EID we are looking RLOCs for 
         NLA_PUT_U32 will go to flag nla_put_failure: a l'air deprecié
        */
    // NLA_PUT_U32( skb, ELA_EID, eid); 
    // NLA_PUT_U32( skb, ELA_MPTCP_TOKEN, token ); 
    

    rc = nla_put_u32( skb, ELA_MPTCP_TOKEN, token );
    // rc = nla_put_string(skb, ELA_EID, "hello world from kernel space\n");
    if (rc != 0)
    {
        lig_debug( KERN_ERR "could not add token \n");
        return rc;
    }


    rc = nla_put_u32( skb, ELA_EID, eid);
    // rc = nla_put_string(skb, ELA_EID, "hello world from kernel space\n");
    if (rc != 0)
    {
        lig_debug( KERN_ERR "could not add eid \n");
        return rc;
    }



    /* finalize the message */
    genlmsg_end(skb, msg_head);


    /* returns -ESRCH  (= -3) => no such process */
        // todo a envoyer en broadcast
    //struct sk_buff *skb, u32 pid,unsigned int group, gfp_t flags)
    rc = genlmsg_multicast(
        skb,
        0,  /* set own pid to not recevie . 0 looks ok might use uint32_t nl_socket_get_local_port(const struct nl_sock *sk); as well ? */
        // nl_socket_get_local_port(const struct nl_sock *sk);

        lig_multicast_group.id,
        // GFP_ATOMIC should be kept for cases where sleep is totally unacceptable
        // + GFP_KERNEL is more likely to succeed
        GFP_KERNEL
         );


    if(rc != 0)
    {
        lig_debug( KERN_ERR "could not multicast packet: %d\n", rc);

        /* no such process */
        if (rc == -ESRCH)
        {
            lig_debug( KERN_ERR "Shoulb be because daemon is not running\n");

        }
        return -1;
    }

    return 0;

// nla_put_failure:
//     lig_debug( KERN_ERR "could not add payload\n");
//     return -1;
    /* TODO wait for answer */

    /* */
    
}



/*
The parsed Netlink attributes from the request;
if the Generic Netlink family definition specified a Netlink attribute policy
then the attributes would have already been validated.
The doit() handler should do whatever processing is necessary and
eturn zero on success or a negative value on failure.
Negative return values will cause an NLMSG_ERROR message to be sent while a
 zero return value will only cause the NLMSG_ERROR message to be
 sent if the request is received with the NLM_F_ACK flag set.


 struct genl_info {
        u32                     snd_seq;
        u32                     snd_portid;
        struct nlmsghdr *       nlhdr;
        struct genlmsghdr *     genlhdr;
        void *                  userhdr;
        struct nlattr **        attrs;
#ifdef CONFIG_NET_NS
        struct net *            _net;
#endif
        void *                  user_ptr[2]; };
 */
int handle_results(struct sk_buff *skb_2, struct genl_info *info)
{
/*

nl_msg
struct genlmsghdr {
          __u8    cmd;
          __u8    version;
          __u16   reserved;
  };

struct nlmsghdr {
         __u32           nlmsg_len;       Length of message including header
         __u16           nlmsg_type;      Message content
         __u16           nlmsg_flags;     Additional flags
         __u32           nlmsg_seq;       Sequence number
         __u32           nlmsg_pid;       Sending process port ID
 };


    // return (struct nlmsghdr *)((char *)user_hdr -
    //                family->hdrsize -
    //                GENL_HDRLEN -
    //                NLMSG_HDRLEN);


    
    struct nlattr {
            __u16           nla_len;
            __u16           nla_type;
    };
**/
    struct nlattr *nla = 0;
//    struct nlmsghdr *req_nlh = info->nlhdr;
    struct genlmsghdr* pGenlhdr = info->genlhdr;
    struct nlattr **tb;
    // int rc;
    int pos = 0;
    int cmd = 0;
    int ret = 0;
    u32 number_of_rlocs = 0;
    // u32 eid = 0;
    u32 token = 0;
    int rem = 0;

	// char * mydata;


    lig_debug("call to \"%s\" in reaction to sender pid: %d \n",__func__, info->snd_pid );
    lig_debug("Message length: %d \n", info->nlhdr->nlmsg_len );

    cmd = pGenlhdr->cmd;
    lig_debug("Command is: %d, that is \"%s\" n", cmd , getCommandStr(cmd) );
    //,commandsStr[cmd]

    // if (info == NULL)
    // {
    //     lig_debug(KERN_WARNING "genl_info is null\n");
    //     goto out;
    // }

    switch(cmd)
    {
        case ELC_RESULTS:
            lig_debug("recieved - a priori - the number of rlocs for the EID\n");
    /*
    for each attribute there is an index in info->attrs which points to
    a nlattr structure
    in this structure the data is given
     */
            nla = info->attrs[ELA_MPTCP_TOKEN];
            
            if (nla == 0)
            {

                lig_debug("No MPTCP token available for current host \n");
            }
            else {

                token = nla_get_u32(nla);

                lig_debug("Received nla of type %d and len %d. TOken value: \"%#x\"  ", nla->nla_type, nla->nla_len, token);
            }


            // TODO a copier dans le daemon pour voir 
            // nla_for_each_attr(pos, info->nlhdr, LIG_GENL_HDRLEN, )
            // {
            //     lig_debug("Z ");
            // }
             // memset(tb, 0, sizeof(struct nlattr *) * (ELA_MAX + 1));
     
             // nla_for_each_attr(nla, 0, 20, rem) {
             //         u16 type = nla_type(nla);
             //        lig_debug("element of type %c\n",type );
             //         if (type > 0 && type <= ELA_MAX) {
             //                 // if (policy) {
             //                         // err = validate_nla(nla, ELA_MAX, policy);
             //                         // if (err < 0)
             //                    // lig_debug("has a policy\n");
             //                                 // goto errout;
             //                 // }
     
             //                 tb[type] = (struct nlattr *)nla;
             //         }
             // }
            // Normalement c'est parse par nla_parse
            nla = info->attrs[ELA_RLOCS_NUMBER];
            // nla = info->attrs[ELA_EID];


            lig_debug("%p, %p , %p, %p ",info->attrs[ELA_MPTCP_TOKEN], info->attrs[ELA_MAX], info->attrs[ELA_EID], info->attrs[ELA_RLOCS_NUMBER] );
            if (nla)
            {
                // mydata = (char *)nla_data(na);
                number_of_rlocs = nla_get_u32(nla);
                
                // if (mydata == NULL)
                    // lig_debug("error while receiving data\n");
                // else
                // queue_work

                // number of subflows to create per interface
                // *
                
                lig_debug("number of rlocs should create %d \n", number_of_rlocs );
                // lig_debug(KERN_NOTICE "eid %u.%u.%u.%u. Calling kernel function mptcp_generate_paths\n", NIPQUAD(eid) );


                if (token == 0){
                    number_of_local_rlocs = number_of_rlocs;
                }
                // TODO replace 3

                /**
                accept token/number_of subflows to
                - 

                **/
                ret = mptcp_generate_paths( token, number_of_local_rlocs, number_of_rlocs  );
                if( ret < 0)
                {
                    lig_debug("Call to generate paths failed \n" );
                }
                else {
                    lig_debug("call succeded\n" );
                }

                
            }
            else
            {
                lig_debug("no info->attrs\n");
            }

            break;

        case ELC_REQUEST_RLOCS_FOR_EID:
            lig_debug(KERN_WARNING "recieved a priori a request for an eid : should not happen\n");

            return -1;

        case ELC_SET_MAP_RESOLVER:
            lig_debug(KERN_WARNING "recieved a priori a request ELC_SET_MAP_RESOLVER\n");

            return -1;

        default:
            lig_debug(KERN_WARNING "unknown command %d sent\n", cmd);
            return -1;
    }


//     lig_debug("an error occured in %s:\n",__func__);
    return 0;
}







static int __init init_lig_module(void)
{
	int rc = 0;
    // lig_multicast_group = 0;

    lig_debug("LIG MODULE initialization\n");




    /*register new family*/
    // ELC_MAX
	rc = genl_register_family_with_ops(&lig_gnl_family,lig_genl_ops, ARRAY_SIZE(lig_genl_ops) );
	if (rc != 0){
        lig_debug(KERN_WARNING "could not register ops: %i\n",rc);
	// 	genl_unregister_family(&lig_gnl_family);
	// 	rc = genl_register_family(&lig_gnl_family);
	// 	if (rc != 0)
		goto failure;
	}





    // my_timer.function, my_timer.data
    // setup_timer( &my_timer, my_timer_callback, 0 );

    // lig_debug( "Starting timer to fire in 200ms (%ld)\n", jiffies );
    // rc = mod_timer( &my_timer, jiffies + msecs_to_jiffies( TIMER_DELAY) );
    // if (rc)
    // {
    //     lig_debug("Error in mod_timer\n");
    // }

    //
    rc = genl_register_mc_group(&lig_gnl_family, &lig_multicast_group);

    if(rc != 0)
    {
        lig_debug(KERN_WARNING "could not register multicast group: %d\n",rc);
    }



    /**
    register as mptcp path discovery system.
    **/
    if( register_mptcp_path_discovery_system(send_request_for_eid) == 0)
    {
        lig_debug("successfully registered mptcp path discovery system\n");

    }
    else
    {
        lig_debug(KERN_ERR "Could not register mptcp path discovery system\n");
    }


    //! TODO daemon won't run at this stage token = 0
    rc = send_request_for_eid( in_aton( hostEID ), 0 );
    if( rc < 0)
    {
        lig_debug ("Requesting failed\n");
    }

    /**
 * genlmsg_multicast_netns - multicast a netlink message to a specific netns
 * @net: the net namespace
 * @skb: netlink message as socket buffer
 * @pid: own netlink pid to avoid sending to yourself
 * @group: multicast group id
 * @flags: allocation flags
 */
// static inline int genlmsg_multicast_netns(struct net *net, struct sk_buff *skb,
// 					  u32 pid, unsigned int group, gfp_t flags)

	return 0;



failure:
    lig_debug(KERN_ERR "an error occured while inserting the generic netlink example module\n");
    return -1;

}






static void __exit cleanup_lig_module(void)
{

	int ret = 0;

 	lig_debug(KERN_INFO "cleanup_lig_module() called\n");

 	/* do not forget to unregister family
	returns 0 on success
	unregister operations as well
 	*/
	// if(!lig_genl_family_registered)
 //  {
 //      return;
 //  }

  ret = genl_unregister_family(&lig_gnl_family);
 	if( ret != 0)
 	{
 		lig_debug(KERN_WARNING "Could not unregister family, error: %d\n", ret);
 	}

    /* returns 0 or 1 according to previous timer state */
    del_timer( &my_timer );
    // ret = del_timer( &my_timer );
    // if (ret)
    // {
    //     lig_debug("The timer is still in use...\n");
    // }

    unregister_mptcp_path_discovery_system();
        // lig_debug("successfully registered mptcp path discovery system\n");





}


module_init( init_lig_module );
module_exit( cleanup_lig_module );
