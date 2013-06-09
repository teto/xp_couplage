#ifndef LIG_MODULE_H
#define LIG_MODULE_H




/* attributes (variables): the index in this enum is used as a reference for the type,
 *  userspace application has to indicate the corresponding type
 *  the policy is used for security considerations
 */
typedef enum {
    //DOC_EXMPL_A_MSG,
	ELA_RLOCS_NUMBER = 1,	/* number of rlocs u8 */
	ELA_MPTCP_TOKEN,	/* to be able to retrieve correct socket */
	ELA_EID,		/*	= an IP. Only v4 supported as an u32 */
	ELA_MAX

} E_LIG_ATTRIBUTE;

//#define DOC_EXMPL_A_MAX (__DOC_EXMPL_A_MAX - 1)

/* protocol version */
#define LIG_GENL_VERSION 1
#define LIG_GROUP_NAME "lig_daemons"


/*
 * TIPC specific header used in NETLINK_GENERIC requests.
 */
struct lig_genl_msghdr {
	__u32 dest;		/* Destination address */
	__u16 cmd;		/* Command */
	__u16 reserved;		/* Unused */
};

// #define LIG_GENL_HDRLEN	NLMSG_ALIGN(sizeof(struct lig_genl_msghdr))
#define LIG_GENL_HDRLEN	0

/*the name of this family, used by userspace application */
#define LIG_FAMILY_NAME "LIG_FAMILY"



/* commands: enumeration of all commands (functions),
 * used by userspace application to identify command to be ececuted
 */
 typedef enum  {

	/**
	When mptcp asks userspace for the number of rlocs responsible for this EID.
	sends:
	-an EID (only v4 for now => NLA_U32)

	TODO: implement batching mode, asks for several EIDS in a same request
	**/
	ELC_REQUEST_RLOCS_FOR_EID,

	/**
	When userspace returns results, waiting for:
	-the number of rlocs (NLA_U8)
	**/
	ELC_RESULTS,

	/** send eid to use as map resolver **/
	ELC_SET_MAP_RESOLVER,

	/* Facility */
	ELC_MAX
} E_LIG_COMMAND;

// typedef enum E_LIG_COMMAND lig_command_t;

char* commandsStr[ELC_MAX + 1] =
{
	[ELC_REQUEST_RLOCS_FOR_EID] = "ELC_REQUEST_RLOCS_FOR_EID",
	[ELC_RESULTS]	= "ELC_RESULTS",
	[ELC_SET_MAP_RESOLVER] = "ELC_SET_MAP_RESOLVER",
	[ELC_MAX]	= "ELC_MAX"
};


char* attributesStr[ELA_MAX + 1] =
{
	[ELA_RLOCS_NUMBER] = "ELA_RLOCS_NUMBER",
	[ELA_MPTCP_TOKEN] = "ELA_MPTCP_TOKEN",
	[ELA_EID]	= "ELA_EID",
	[ELA_MAX]	= "ELA_MAX"
};

#define NIPQUAD(addr) \
      ((unsigned char *)&addr)[0], \
         ((unsigned char *)&addr)[1], \
         ((unsigned char *)&addr)[2], \
         ((unsigned char *)&addr)[3]



//int 


// Unsed
// struct s_lig_result {
//     int number_of_remote_rlocs;
//     int number_of_local_rlocs;
// };

// struct s_lig_request {
//     int remote_eid;
//     int local_eid;
// //    int number_of_local_rlocs;
// };


//genlmsghdr* genl_retrieve_genlhdrfromnlhdr()
//{
//	return (struct nlmsghdr *)((char *)user_hdr -
//				   family->hdrsize -
//				   GENL_HDRLEN -
//				   NLMSG_HDRLEN);
//
//}

         /* attribute policy: defines which attribute has which type (e.g int, char * etc)
 * possible values defined in net/netlink.h
 netlink attribute / action  ?
 */
static struct nla_policy lig_policies[ ELA_MAX ] = {
	// [ELA_RLOCS_NUMBER] = { .type = NLA_U8 },
	[ELA_RLOCS_NUMBER] = { .type = NLA_U32 },

    /**
    An EID is an IP, for now only IPv4 is supported.
    **/
    [ELA_EID] = { .type = NLA_U32 },

    /* usefeul to idetify associated socket, know if it's still active  */
    [ELA_MPTCP_TOKEN] = { .type = NLA_U32 }
	// [ELA_EID] = { .type = NLA_NUL_STRING , .len = 120}
	// [ELA_MAX ]
};



// nla_for_each_attr

#endif
