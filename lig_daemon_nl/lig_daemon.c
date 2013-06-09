/**
@author: Matthieu Coudron

Libraries needed:
-libgenl
-libnl
-libexplain



**/


//#include <netlink/socket.h>
//#include <netlink/netlink.h>
//#include <linux/genetlink.h>
#include <netlink/netlink.h>
#include <netlink/genl/genl.h>
#include <netlink/genl/ctrl.h>
#include <netlink/genl/mngt.h>
#include <linux/types.h>
#include <libexplain/execvp.h>
//#include <asm/types.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h> // for exe functions

#include"../lig_module/lig_module.h"



static struct nl_sock *sk = 0;
static int family_id = -1;
static int group_id = -1;


#define PATH_TOWARDS_PROGRAM  "/home/teto/lig/process_lig_output.sh"

/***


http://www.linuxfoundation.org/collaborate/workgroups/networking/genericnetlinkhowto#Registering_A_Family

**/

/**
should be able to get peer port automatically
uint32_t nl_socket_get_local_port(const struct nl_sock *sk);
nl_socket_set_peer_port(struct nl_sock *sk, uint32_t port);
, u_int32_t  pid
*/
static int send_rlocs_list_for_eid( u_int32_t eid,u_int32_t token)
{
    struct nl_msg *msg = 0;
    void *user_hdr = 0;
    int ret = 0;
    int childExitStatus = 0;
    // int number_of_rlocs = 0;
    // TODO a renommer en remote
    u_int32_t number_of_rlocs = 0;
    // u32
//    char strEID[INET_ADDRSTRLEN];
    char* strEID;
    char commandStr[100];
    struct in_addr addr;

/*


char ip[] = "192.168.1.102";
long long_address = inet_addr (ip) ;
char *dot_ip = inet_ntoa(long_address);

*/
    addr.s_addr = eid;

    strEID = inet_ntoa( addr );
//    snprintf(strEID,"%u.%u.%u.%u", NIPQUAD(eid) );

    printf("EID: %s\n", strEID);


    if (!(msg = nlmsg_alloc()))
    {
        printf("Could not allocate a new message");
        return -1;
    }


//    msg = nlmsg_new()

    /* send with type= -1 */
    user_hdr = genlmsg_put(msg,
                           0,        /* port	Netlink port or NL_AUTO_PORT */
                           0,     /* Sequence number of message or NL_AUTO_SEQ*/
                           family_id,       /* Numeric family identifier*/
                            LIG_GENL_HDRLEN,     /* Length of user header*/
                            0,               /* flags (optional ) */
                           ELC_RESULTS,      /* command identifier */
                           LIG_GENL_VERSION      /* version */
                           );


    if (!user_hdr)
    {
        printf("Could not generate a new message\n");
        nlmsg_free(msg);
        return -1;
    }


    /* last parameter should be always NULL */
//    char* argv[] = { PATH_TOWARDS_PROGRAM, strEID, 0 };
    snprintf(commandStr, 100, "%s %s", PATH_TOWARDS_PROGRAM, strEID);
    printf("LAunching program with command:\t%s\n", commandStr) ;


/* man system : system() executes a command specified in command by calling /bin/sh -c command, and returns after the command has been completed */
/* execvp terminates program (except if error, so either e fork or we use system instead */
//    ret = execvp(argv[0], argv);

    // REnvoie tjrs 1 (pr les besoins de la simulation)

    /** need to use macros since **/
    childExitStatus = system(commandStr);

//    if( childExitStatus == -1)
//    {
//
//        printf("fork failed \n");
//    }


    if(!WIFEXITED(childExitStatus))
    {
      printf("System call terminated abnormally!\n");

      if(WIFSIGNALED(childExitStatus) )
      {
        printf("The system call was terminated with the signal %d", WTERMSIG(childExitStatus));
      }
        return -1;
    }
    else
    {
        number_of_rlocs= WEXITSTATUS(childExitStatus);
      printf("System call terminated normaly with the return value: %d\n", childExitStatus);
    }



//
//    printf("Call of %s just finished \n", PATH_TOWARDS_PROGRAM) ;
//
//    if(ret < 0)
//    {
//        //fprintf(stderr, "%s\n", );
//        printf("Command failed: %s\n", strerror(ret) );
//        nlmsg_free(msg);
//        // ret = 0;
//        return -1;
//    }

//    number_of_rlocs = ret;

    printf("\"%d\" rlocs associated with EID: %s\n", number_of_rlocs, strEID );

//    system("process_lig_output.sh");
//    number_of_rlocs = execl("", ntop_iten(), NULL);

    /* puts the number of rlocs available for the requested eid */
    /* mest , attribute type , value */
    // NLA_PUT_U32 will go to flag nla_put_failure:

    /* MEGA HACK
     TODO la ca devrait etre un un ELA_RLOC_NUMBER normalement mais ca bug, le module arrive pas a le parser
     */
    // ret = nla_put_u32(msg, ELA_EID, number_of_rlocs );
    ret = nla_put_u32(msg, ELA_RLOCS_NUMBER, number_of_rlocs );
    // ret = nla_put_u32(msg, ELA_RLOCS_NUMBER, number_of_rlocs );
        // ret = nla_put_u32(msg, ELA_EID, number_of_rlocs );
            // ret = nla_put_u32(msg, ELA_MPTCP_TOKEN, number_of_rlocs );
    if(ret != 0)
    {
        printf("Could not add ELA_RLOCS_NUMBER\n");
//        goto skb_failure;
        nlmsg_free(msg);
        return ret;
    }


    ret = nla_put_u32(msg, ELA_MPTCP_TOKEN, token );
    if(ret != 0)
    {
        printf("Could not add ELA_MPTCP_TOKEN\n");
//        goto skb_failure;
        nlmsg_free(msg);
        return ret;
    }

    printf("Sending answer\n" );

    ret = nl_send_auto_complete(sk, msg) ;
//    ret = nl_send_auto(sk, msg) ;
	if (ret < 0) {
		printf("error sending message\n");
//		goto skb_failure;
	}



    nlmsg_free(msg);

    return ret;
}



static int parse_cb(struct nl_msg *msg, void *arg)
{

    struct nlmsghdr *nlh = 0;
    struct genlmsghdr* genlh = 0;
    int cmd= 0;
    u_int32_t token = 0;
    struct nlattr* attrs[ELA_MAX];
    struct nlattr* na = 0;
    u_int32_t eid = 0;
    int ret = 0;
    u_int32_t sender_pid = 0;
    printf("%s callback called\n",__func__);
    nlh = nlmsg_hdr(msg);

/**
 * Return pointer to Generic Netlink header
 * @arg nlh		Netlink message header
 *
 * @return Pointer to Generic Netlink message header
 */
//struct genlmsghdr *genlmsg_hdr(struct nlmsghdr *nlh)
//{
//	return nlmsg_data(nlh);
//}
    sender_pid = nlh->nlmsg_pid;
    printf("Sender port id: %u, with flags: %d and type %d, seq %u \n", sender_pid, nlh->nlmsg_flags ,nlh->nlmsg_type, nlh->nlmsg_seq);



    genlh = nlmsg_data(nlh);

    if(!genlh)
    {
        printf("Could not retrieve generic netlink header\n");
        return -1;
    }

    cmd = genlh->cmd;
    printf("Received Command : %d with version %d\n", cmd , genlh->version);


/**
genlmsg_attrdataReturn pointer to message attributes.
**/
    ret = nla_parse   (
        attrs,
        ELA_MAX,            /* int     maxtype,*/
        genlmsg_attrdata(genlh, LIG_GENL_HDRLEN ),                  /*struct nlattr *     head,*/
        genlmsg_attrlen(genlh,LIG_GENL_HDRLEN),    /*int     len,*/
        // 0                   /* struct nla_policy *     policy */
        lig_policies
        );


    // ret = genlmsg_parse(
    //                     nlh,
    //                     LIG_GENL_HDRLEN,
    //                     attrs,
    //                     ELA_MAX,
    //                     0
    //                     );
    if (ret < 0)
    {
        printf("Could not parse attributes" );
        return -1;
    }

//    attrs = genlmsg_attrdata(genlh, LIG_GENL_HDRLEN);
//    if(!attrs)
//    {
//        printf(" empty payload ?!" );
//        return -1;
//    }


    switch(cmd)
    {

    case ELC_REQUEST_RLOCS_FOR_EID:
            printf("recieved request for an EID...\n");

            // TODO il faut lire les attributs
            na = attrs[ELA_EID];
            if (na)
            {
                // TODO creer une structure pour ca carrement
                // mydata = (char *)nla_data(na);
                eid = nla_get_u32(attrs[ELA_EID]);
                token = nla_get_u32(attrs[ELA_MPTCP_TOKEN]);
                // if (mydata == NULL)
                    // printk("error while receiving data\n");
                // else
                printf( "EID received : %u.%u.%u.%u with local token %#x \n", NIPQUAD(eid), token );

                // answers request
                if(send_rlocs_list_for_eid(eid,token ) < 0)
                {
                    printf("Could not answer request for eid \n");//, &eid
                    return -1;
                }

            }
            else
            {
                printf("\nerror: missing EID\n");
                return -1;
            }
        // TODO call lig program, parse results and send them back
        // recuperer l'EID et le faire suivre

            return 0;

    default :
        printf("Default case, cmd %d", cmd);
        break;
    }
//   if ((err = genlsmg_parse(nlmsg_nlh(msg), sizeof(struct my_hdr), attrs,
//                            MY_TYPE_MAX, attr_policy)) < 0)
//        // ERROR

//    genlmsghdr *genlmsg_hdr()


//	return genl_handle_msg(msg, NULL);
    return 0;
}



int main()
{


    int ret = 0;
//    int family_id = 0;
//    int pid = 0;
//    struct sk_buff *skb = 0;
//    void *msg_head;

    struct nl_msg *msg = 0;
//     struct s_lig_result *user_hdr;

    sk = 0;

    printf("Starting LIG DAEMON\n");

    sk = nl_socket_alloc();

    if(!sk) {
        printf("could not allocate socket\n");
        return EXIT_FAILURE;
    }


//nl_addr2str(

    if(nl_connect(sk, NETLINK_GENERIC) != 0)
    {
        printf("could not connect socket\n");
        goto fail_connect;

    }


    printf("Disabling sequence number for this socket\n");
//    nl_socket_disable_seq_check(sk);

     nl_socket_disable_auto_ack(sk);

//

    /** 2nd parameter refers to family name defined in gnl_family.name */
    family_id = genl_ctrl_resolve (sk, LIG_FAMILY_NAME);
    if(family_id < 0 )
    {
        printf("could not find family id\n");
        goto failure;
    }

    printf("Family id:\t%d\n", family_id);


    group_id = genl_ctrl_resolve_grp (sk, LIG_FAMILY_NAME, LIG_GROUP_NAME);
    if(group_id  < 0 )
    {
        printf("could not find group id \n");
        goto failure;
    }

    printf("Group id:\t%d\n",group_id);


    ret = nl_socket_add_membership(sk, group_id);
    if(ret != 0)
    {
        printf("could not register to group %d\n",group_id);
        goto failure;
    }
    else
        printf("successfully registered to group id:\t%d\n",group_id);


    // TODO

//    printf("Family No:\t%d\n", family_id);





	/* set the callback function to receive answers to recv_msg
        Fitlers message:
            - NL_CB_MSG_IN = > Called for every message received
            - NL_CB_VALID
        Available Callback functions:
            -NL_CB_DEBUG or NL_CB_VERBOSE to debug
            -NL_CB_CUSTOM use user's defined cb


	*/

	if (nl_socket_modify_cb( sk, NL_CB_VALID, NL_CB_CUSTOM, parse_cb, NULL) < 0) {
		printf("error setting callback function\n");

		goto skb_failure;
	}

    printf("Waiting for request\n");



    /**
    kill applications
    **/
    while(1)
    {

        /* receive the answer */
        // TODO ajouter un while ici pour traiter toutes les requetes
        // TODO erreur au niveau des sequences
        ret = nl_recvmsgs_default( sk );
        // - 12 = ENOENT normal c parce que personne n'écoute !!!
        printf("Just received a packet. Return value %d: %s.\n", ret, strerror(ret) );
        if( ret < 0)
        {
            printf("Error: %s\n", nl_geterror(ret) );
        }


    }



    // free allocated struct

    nl_socket_free(sk);


    printf("End of  DAEMON\n");
    return EXIT_SUCCESS;



skb_failure:
    nlmsg_free(msg);

failure:
fail_connect:
    nl_socket_free(sk);


    return EXIT_FAILURE;
}
