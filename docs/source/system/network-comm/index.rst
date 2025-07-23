========
datacall
========

此模块包含了PDP Context配置和获取、激活、去激活以及获取模组的IP信息等功能。

DataCall是通信模块建立数据连接的过程，目的是让设备通过运营商的蜂窝网络接入互联网或私有网络。

设备接入运营商网络之后，通过pdp激活流程得到运营商下发的IP地址。设备使用该IP地址，可用于TCP,UDP,HTTP,MQTT等网络协议栈业务的通信。

.. list-table:: DataCall 函数列表
   :widths: 30 70
   :header-rows: 1

   * - 函数
     - 描述
   * - qosa_datacall_attach
     - 激活或者去激活网络
   * - qosa_datacall_wait_attached
     - 等待注网成功
   * - qosa_datacall_is_defined
     - 查询一个指定的PDP是否为已定义状态
   * - qosa_datacall_set_pdp_context
     - 设置特定PDP的PDP context
   * - qosa_datacall_delete_pdp_context
     - 删除特定PDP的PDP context
   * - qosa_datacall_get_pdp_context
     - 获取特定PDP的PDP context
   * - qosa_datacall_set_pdp_auth
     - 设置特定PDP的PDP auth context
   * - qosa_datacall_get_pdp_auth
     - 获取特定PDP的PDP auth context
   * - qosa_datacall_set_pdp_qos
     - 定义特定PDP的QoS profile
   * - qosa_datacall_get_pdp_qos
     - 获取特定PDP的QoS profile
   * - qosa_datacall_conn_new
     - 生成一个特定功能域的连接对象
   * - qosa_datacall_start
     - 打开特定datacall连接对象(同步)
   * - qosa_datacall_start_async
     - 打开特定datacall连接对象(异步接口)
   * - qosa_datacall_stop
     - 关闭特定datacall连接对象(同步接口)
   * - qosa_datacall_stop_async
     - 关闭特定datacall连接对象(异步接口)
   * - qosa_datacall_get_status
     - 获取特定datacall连接对象的连接状态
   * - qosa_datacall_get_ip_info
     - 获取特定datacall连接对象的详细信息
   * - qosa_datacall_get_traffic_statistics
     - 获取上下行流量统计信息
   * - qosa_datacall_clear_traffic_statistics
     - 清除上下行流量统计信息
   * - qosa_datacall_save_traffic_statistics
     - 保存上下行流量信息到NV中
   * - qosa_datacall_set_pdp_timer
     - 配置PDP激活/去激活定时器配置
   * - qosa_datacall_get_pdp_timer
     - 获取PDP激活/去激活定时器配置信息

--------------------
1 网络的激活管理
--------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.1 qosa_datacall_attach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

    ``qosa_datacall_errno_e qosa_datacall_attach(qosa_uint8_t simid, qosa_uint8_t method, datacall_callback_cb_ptr cb, void* ctx)``

- 功能描述
    注册或者反注册网络。

- 参数说明

.. list-table:: qosa_datacall_attach接口参数说明列表
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - method
     - qosa_uint8_t
     - 是
     - 参考qosa_datacall_attach_stat_e
     - 注册或反注册网络

   * - cb
     - datacall_callback_cb_ptr
     - 是
     - 无
     - 异步回调函数

   * - ctx
     - void*
     - 是
     - 无
     - 扩展参数

qosa_datacall_attach_stat_e枚举值

.. code:: c

    typedef enum
    {
      QOSA_DATACALL_DETACH, 
      QOSA_DATACALL_ATTACH, 
    } qosa_datacall_attach_stat_e;

.. list-table:: DataCall qosa_datacall_attach_stat_e枚举值说明
   :header-rows: 1

   * - 枚举值
     - 说明
   * - QOSA_DATACALL_DETACH
     - 反注册网络
   * - QOSA_DATACALL_ATTACH
     - 注册网络


- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值。

- 使用注意事项

    该函数为异步函数。

.. _qosa_datacall_errno_e:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.1.1 qosa_datacall_errno_e
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
对应qosa_datacall_errno_e错误返回值有以下几种情况：

.. code-block:: c

   typedef enum datacall_err
   {
       QOSA_DATACALL_OK = 0,
       QOSA_DATACALL_ERR_OPERATION_NOT_ALLOWED   = 3 | QOSA_ERRCODE_DATACALL_BASE, /*!< operation not allowed */
       QOSA_DATACALL_ERR_OPERATION_NOT_SUPPORTED = 4 | QOSA_ERRCODE_DATACALL_BASE, /*!< operation not supported */
       QOSA_DATACALL_ERR_MEMORY_FULL             = 20 | QOSA_ERRCODE_DATACALL_BASE, /*!< memory full */
       QOSA_DATACALL_ERR_MEMORY_FAILURE          = 23 | QOSA_ERRCODE_DATACALL_BASE, /*!< memory failure */
       QOSA_DATACALL_ERR_INVALID_PARAM           = 53 | QOSA_ERRCODE_DATACALL_BASE, /*!< invalid parameter */
       QOSA_DATACALL_ERR_EXECUTE                 = 1 | (QOSA_ERRCODE_DATACALL_BASE + QOSA_AT_ERR_OFS),
       QOSA_DATACALL_ERR_TIMEOUT,                          /*!< 网络注册超时 */
       QOSA_DATACALL_ERR_NO_ACTIVE,                        /*!< PDP未激活 */
       QOSA_DATACALL_ERR_PDP_NO_DEFINED,                   /*!< PDP未定义错误 */
   } qosa_datacall_errno_e;

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.2 qosa_datacall_wait_attached
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_bool_t qosa_datacall_wait_attached(qosa_uint8_t simid, qosa_uint32_t timeout)

- 功能描述
    执行时判断当前网络是否注册成功，如果当前没有注册成功，则等待一段时间返回网络注册结果。

- 参数说明

.. list-table:: qosa_datacall_wait_attached参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - timeout
     - qosa_uint32_t
     - 是
     - 0x00000000-0xFFFFFFFF，单位ms
     - 超时时间，单位ms

- 返回值说明

    注网成功返回 ``QOSA_TRUE``，超时返回 ``QOSA_FALSE``

- 使用注意事项

    调用本接口后, 将在超时时间内间歇性检查注网状态(阻塞方式), 如果检查到时成功注网, 则退出本API。

------------------------
2 PDP context管理和使用
------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.1 qosa_datacall_is_defined
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_bool_t qosa_datacall_is_defined(qosa_uint8_t simid, qosa_uint8_t pdpid)

- 功能描述
    查询一个指定的PDP是否为已定义状态。

- 参数说明

.. list-table:: qosa_datacall_is_defined参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

- 返回值说明

    已定义返回 ``OSA_TRUE``，未定义返回 ``OSA_FALSE``。

- 使用注意事项

    已定义状态: 用户侧配置了该PDP的profile, 视为用户侧定义。


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.2 qosa_datacall_set_pdp_context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_set_pdp_context(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_pdp_context_t* pdp_ctx)

- 功能描述
    查询一个指定的PDP是否为已定义状态。

- 参数说明

.. list-table:: qosa_datacall_set_pdp_context参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - pdp_ctx
     - qosa_pdp_context_t*
     - 是
     - 无
     - pdp context

.. _qosa_pdp_context_t:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2.2.1 qosa_pdp_context_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef struct
    {
        qosa_uint8_t pdp_type;                                 /*!< PDP类型, qosa_pdp_type_e */

        qosa_bool_t apn_valid;                                 /*!< APN 是否被配置 */
        char        apn[QOSA_APN_MAX_LEN + 1];                 /*!< PDP激活的APN */

        qosa_bool_t    ipv4_ip_valid;                          /*!< IPv4地址是否被配置 */
        qosa_ip_addr_t ipv4_ip;                                /*!< 用户配置的IPv4地址 */

        qosa_bool_t    ipv6_ip_valid;                          /*!< IPv6地址是否被配置 */
        qosa_ip_addr_t ipv6_ip;                                /*!< 用户配置的IPv6地址 */

        qosa_bool_t               data_comp_valid;             /*!< 数据压缩是否被配置 */
        qosa_pdp_data_comp_type_e data_comp;                   /*!< 数据压缩类型 */

        qosa_bool_t               head_comp_valid;             /*!< 头部压缩是否被配置 */
        qosa_pdp_head_comp_type_e head_comp;                   /*!< 头部压缩类型 */

        qosa_bool_t                     ipv4_addr_alloc_valid; /*!< IPv4地址分配是否被配置 */
        qosa_pdp_ipv4_addr_alloc_type_e ipv4_addr_alloc;       /*!< IPv4地址分配类型 */

        qosa_bool_t             request_type_valid;            /*!< PDP请求类型是否被配置 */
        qosa_pdp_request_type_e request_type;                  /*!< PDP请求类型 */

    #ifdef CONFIG_QOSA_NW_NR_SUPPORT
        qosa_bool_t         ssc_mode_valid;  /*!< SCC mode 是否被配置 */
        qosa_pdp_ssc_mode_e ssc_mode;        /*!< SSC mode */

        qosa_bool_t       s_nssai_valid;     /*!< S-NSSAI是否被配置 */
        qosa_nw_s_nssai_t s_nssai;           /*!< S-NSSAI */

        qosa_bool_t  pref_access_type_valid; /*!< preferred access type 是否被配置 */
        qosa_uint8_t pref_access_type;       /*!< preferred access type 0:3GPP 1:Non-3GPP */

        qosa_bool_t  allow_on_req_valid;     /*!< allow on request 是否被配置 */
        qosa_uint8_t allow_on_req;           /*!< allow on request 0:不允许 1:允许 */
    #endif                                   // CONFIG_QOSA_NW_NR_SUPPORT
    } qosa_pdp_context_t;

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    已定义状态: 用户侧配置了该PDP的profile, 视为用户侧定义。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.3 qosa_datacall_delete_pdp_context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_delete_pdp_context(qosa_uint8_t simid, qosa_uint8_t pdpid)

- 功能描述
    删除特定PDP的PDP context。

- 参数说明

.. list-table:: qosa_datacall_delete_pdp_context参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID


- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.4 qosa_datacall_get_pdp_context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_pdp_context(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_pdp_context_t* pdp_ctx)

- 功能描述
    获取特定PDP的PDP context。

- 参数说明

.. list-table:: qosa_datacall_get_pdp_context参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - pdp_ctx
     - qosa_pdp_context_t*
     - 是
     - 0-15
     - pdp context

qosa_pdp_context_t结构体含义参考 :ref:`qosa_pdp_context_t`

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.5 qosa_datacall_set_pdp_auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_set_pdp_auth(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_pdp_auth_context_t* auth_ctx)

- 功能描述
    设置特定PDP的PDP auth context。

- 参数说明

.. list-table:: qosa_datacall_set_pdp_auth参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - pdp_ctx
     - qosa_pdp_auth_context_t*
     - 是
     - 无
     - PDP鉴权参数

.. _qosa_pdp_auth_context_t:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2.5.1 qosa_pdp_auth_context_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef struct
    {
        qosa_bool_t          auth_valid;                               /*!< Auth_type是否被配置 */
        qosa_pdp_auth_type_e auth_type;                                /*!< PDP鉴权类型 */
        qosa_bool_t          user_valid;                               /*!< User 是否被配置 */
        char                 username[QOSA_PDP_USER_NAME_MAX_LEN + 1]; /*!< PDP用户名 */
        qosa_bool_t          pass_valid;                               /*!< password 是否被配置 */
        char                 password[QOSA_PDP_USER_PWD_MAX_LEN + 1];  /*!< PDP密码 */
    } qosa_pdp_auth_context_t;

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.6 qosa_datacall_get_pdp_auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_pdp_auth(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_pdp_auth_context_t* auth_ctx)

- 功能描述
    获取特定PDP的PDP auth context。

- 参数说明

.. list-table:: qosa_datacall_get_pdp_auth参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - pdp_ctx
     - qosa_pdp_auth_context_t*
     - 是
     - 无
     - pdp 鉴权参数


qosa_pdp_auth_context_t结构体含义参考 :ref:`qosa_pdp_auth_context_t`

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.7 qosa_datacall_set_pdp_qos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c
    
    qosa_datacall_errno_e qosa_datacall_set_pdp_qos(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_pdp_qos_profile_t* qos_profile)

- 功能描述
    定义特定PDP的QoS profile。

- 参数说明

.. list-table:: qosa_datacall_set_pdp_qos参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - qos_profile
     - qosa_pdp_qos_profile_t*
     - 是
     - 无
     - PDP QoS参数

.. _qosa_pdp_qos_profile_t:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2.7.1 qosa_pdp_qos_profile_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef struct
    {
        qosa_uint8_t precedence;  /*!< specifies the precedence class */
        qosa_uint8_t delay;       /*!< specifies the delay class */
        qosa_uint8_t reliability; /*!< specifies the reliability class */
        qosa_uint8_t peak;        /*!< specifies the peak throughput class */
        qosa_uint8_t mean;        /*!< specifies the mean throughput class */
    } qosa_pdp_qos_profile_t;

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.8 qosa_datacall_get_pdp_qos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_pdp_qos(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_pdp_qos_profile_t* qos_profile)

- 功能描述
    获取特定PDP的QoS profile.

- 参数说明

.. list-table:: qosa_datacall_get_pdp_qos参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - qos_profile
     - qosa_pdp_qos_profile_t*
     - 是
     - 无
     - PDP QoS参数


qosa_pdp_qos_profile_t结构体含义参考 :ref:`qosa_pdp_qos_profile_t`


- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

---------------------
3 DNS地址的配置和查询
---------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3.1 qosa_datacall_get_dns_addr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_dns_addr(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_datacall_dns_t* dns)

- 功能描述
    获取dns服务器IP地址.

- 参数说明

.. list-table:: qosa_datacall_get_dns_addr参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - dns
     - qosa_datacall_dns_t*
     - 是
     - 无
     - DNS地址配置

.. _qosa_datacall_dns_t:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.1.1 qosa_datacall_dns_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef struct
    {
        qosa_ip_addr_t pri_dns;  /*!< cache中的DNS首地址 */
        qosa_ip_addr_t sec_dns;  /*!< cache中的DNS辅地址 */
        qosa_ip_addr_t pri6_dns; /*!< cache中的DNS首地址 */
        qosa_ip_addr_t sec6_dns; /*!< cache中的DNS辅地址 */
    } qosa_datacall_dns_t;

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3.2 qosa_datacall_set_dns_addr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_set_dns_addr(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_datacall_dns_t* dns)

- 功能描述
    设置dns服务器IP地址.

- 参数说明

.. list-table:: qosa_datacall_set_dns_addr参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - dns
     - qosa_datacall_dns_t*
     - 是
     - 无
     - DNS地址配置

qosa_datacall_dns_t结构体含义参考 :ref:`qosa_datacall_dns_t`

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

----------------------------------------------------------
4 datacall连接对象的管理和使用
----------------------------------------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4.1 qosa_datacall_conn_new
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_conn_t qosa_datacall_conn_new(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_datacall_conn_type_e conn_type)

- 功能描述
    生成一个特定功能域的连接对象.

- 参数说明

.. list-table:: qosa_datacall_conn_new参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - pdpid
     - qosa_uint8_t
     - 是
     - 0-15
     - PDP ID

   * - conn_type
     - qosa_datacall_conn_type_e
     - 是
     - 参考qosa_datacall_conn_type_e
     - datacall连接应用的功能域

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
4.1.1 qosa_datacall_conn_type_e
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef enum
    {
        QOSA_DATACALL_CONN_USBNET = 1, /*!< 指向usbnet连接功能 */
        QOSA_DATACALL_CONN_PPP,        /*!< 指向PPP连接功能 */
        QOSA_DATACALL_CONN_TCPIP,      /*!< 指向所有的协议栈板块功能, 如tcpip, MQTT, FTP, 等等 */
        QOSA_DATACALL_CONN_UNDEFINED,  /*!< 非特定连接域 */
        QOSA_DATACALL_CONN_MAX,
    } qosa_datacall_conn_type_e;

- 返回值说明

    返回连接对象，如果参数非法，将返回 ``OSA_DATACALL_CONN_INVALID``。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4.2 qosa_datacall_start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_start(qosa_datacall_conn_t conn, qosa_uint32_t max_wait_time)

- 功能描述
    打开特定datacall连接对象(同步).

- 参数说明

.. list-table:: qosa_datacall_start参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - conn
     - qosa_datacall_conn_t
     - 是
     - 无
     - 数据拨号连接域对象

   * - max_wait_time
     - qosa_uint32_t
     - 是
     - 单位s
     - 最大超时时间, 0表示使用默认超时时间


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
4.2.1 qosa_datacall_conn_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef qosa_base_t qosa_datacall_conn_t;

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4.3 qosa_datacall_start_async
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_start_async(qosa_datacall_conn_t conn, qosa_uint32_t max_wait_time, datacall_callback_cb_ptr cb, void* ctx)

- 功能描述
    打开特定datacall连接对象(异步接口).

- 参数说明

.. list-table:: qosa_datacall_start_async参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - conn
     - qosa_datacall_conn_t
     - 是
     - 无
     - 数据拨号连接域对象

   * - max_wait_time
     - qosa_uint32_t
     - 是
     - 单位s
     - 最大超时时间, 0表示使用默认超时时间

   * - cb
     - datacall_callback_cb_ptr
     - 是
     - 无
     - 异步回调函数

   * - ctx
     - void*
     - 是
     - 无
     - 扩展参数


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
4.2.1 qosa_datacall_conn_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef qosa_base_t qosa_datacall_conn_t;

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4.4 qosa_datacall_stop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_stop(qosa_datacall_conn_t conn, qosa_uint32_t max_wait_time)

- 功能描述
    关闭特定datacall连接对象(同步接口).

- 参数说明

.. list-table:: qosa_datacall_stop参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - conn
     - qosa_datacall_conn_t
     - 是
     - 无
     - 数据拨号连接域对象

   * - max_wait_time
     - qosa_uint32_t
     - 是
     - 单位s
     - 最大超时时间, 0表示使用默认超时时间


- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4.5 qosa_datacall_stop_async
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_stop_async(qosa_datacall_conn_t conn, qosa_uint32_t max_wait_time, datacall_callback_cb_ptr cb, void* ctx)

- 功能描述
    关闭特定datacall连接对象(异步接口).

- 参数说明

.. list-table:: qosa_datacall_stop_async参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - conn
     - qosa_datacall_conn_t
     - 是
     - 无
     - 数据拨号连接域对象

   * - max_wait_time
     - qosa_uint32_t
     - 是
     - 单位s
     - 最大超时时间, 0表示使用默认超时时间

   * - cb
     - datacall_callback_cb_ptr
     - 是
     - 无
     - 异步回调函数

   * - ctx
     - void*
     - 是
     - 无
     - 扩展参数

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4.6 qosa_datacall_get_status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_bool_t qosa_datacall_get_status(qosa_datacall_conn_t conn)

- 功能描述
    获取特定datacall连接对象的连接状态.

- 参数说明

.. list-table:: qosa_datacall_get_status参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - conn
     - qosa_datacall_conn_t
     - 是
     - 无
     - 数据拨号连接域对象


- 返回值说明

    0:非激活状态 
    1:已激活状态。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4.7 qosa_datacall_get_ip_info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_ip_info(qosa_datacall_conn_t conn, qosa_datacall_ip_info_t* info)

- 功能描述
    获取特定datacall连接对象的详细信息.

- 参数说明

.. list-table:: qosa_datacall_get_ip_info参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - conn
     - qosa_datacall_conn_t
     - 是
     - 无
     - 数据拨号连接域对象

   * - info
     - qosa_datacall_ip_info_t*
     - 是
     - 无
     - 连接对象信息

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。


- 使用注意事项

    无。

------------------
5 流量信息管理功能
------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5.1 qosa_datacall_get_traffic_statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_traffic_statistics(qosa_uint8_t simid, qosa_datacall_traffic_statistics_t* traffic_statistics)

- 功能描述
    获取上下行流量统计信息.

- 参数说明

.. list-table:: qosa_datacall_get_traffic_statistics参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - traffic_statistics
     - qosa_datacall_traffic_statistics_t*
     - 是
     - 无
     - 获取的流量统计信息

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
5.1.1 qosa_datacall_traffic_statistics_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef struct
    {
        qosa_uint64_t total_uplink_bytes;             /*!< 总上行流量, 单位字节 */
        qosa_uint64_t total_downlink_bytes;           /*!< 总下行流量, 单位字节 */

        qosa_uint64_t uplink_bytes[QOSA_PDPID_MAX];   /*!< 单路PDP的上行流量, 单位字节 */
        qosa_uint64_t downlink_bytes[QOSA_PDPID_MAX]; /*!< 单路PDP的下行流量, 单位字节 */
    } qosa_datacall_traffic_statistics_t;

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5.2 qosa_datacall_clear_traffic_statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_clear_traffic_statistics(qosa_uint8_t simid)

- 功能描述
    清除上下行流量统计信息.

- 参数说明

.. list-table:: qosa_datacall_get_traffic_statistics参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。


- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5.3 qosa_datacall_save_traffic_statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_save_traffic_statistics(qosa_uint8_t simid)

- 功能描述
    保存上下行流量信息到NV中.

- 参数说明

.. list-table:: qosa_datacall_save_traffic_statistics参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

---------------
6 pdp定时器管理
---------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
6.1 qosa_datacall_set_pdp_timer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_set_pdp_timer(qosa_uint8_t simid, qosa_uint8_t rat, qosa_uint8_t procedure, qosa_datacall_pdp_timer_t* pdp_timer)

- 功能描述
    配置PDP激活/去激活定时器配置.

- 参数说明

.. list-table:: qosa_datacall_set_pdp_timer参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - rat
     - qosa_uint8_t
     - 是
     - 参考qosa_network.h中的qosa_nw_rat_e
     - 待获取的定时器归属的rat

   * - procedure
     - qosa_uint8_t
     - 是
     - 参考qosa_datacall_pdp_act_opt_e
     - 待获取的定时器的类型, 激活或去激活操作用的定时器

   * - pdp_timer
     - qosa_datacall_pdp_timer_t*
     - 是
     - 无
     - 定时器配置

.. _qosa_datacall_pdp_timer_t:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
6.1.1 qosa_datacall_pdp_timer_t
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef struct
    {
        qosa_uint8_t counts;      /*!< PDP重试次数, 0表示不重试, 即代表只执行一次PDP active或者deactivate操作 */
        qosa_uint8_t timer_value; /*!< 重试时间 (单位s) */
    } qosa_datacall_pdp_timer_t;

.. _qosa_datacall_pdp_act_opt_e:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
6.1.2 qosa_datacall_pdp_act_opt_e
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: c

    typedef enum
    {
        QOSA_PDP_OPT_DEACTIVE = 0,
        QOSA_PDP_OPT_ACTIVE = 1,
        QOSA_PDP_OPT_MAX
    } qosa_datacall_pdp_act_opt_e;


- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
6.2 qosa_datacall_get_pdp_timer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_pdp_timer(qosa_uint8_t simid, qosa_uint8_t rat, qosa_uint8_t procedure, qosa_datacall_pdp_timer_t* pdp_timer)

- 功能描述
    获取PDP激活/去激活定时器配置信息.

- 参数说明

.. list-table:: qosa_datacall_get_pdp_timer参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - simid
     - qosa_uint8_t
     - 是
     - 0-1
     - sim卡ID

   * - rat
     - qosa_uint8_t
     - 是
     - 参考qosa_network.h中的qosa_nw_rat_e
     - 待获取的定时器归属的rat

   * - procedure
     - qosa_uint8_t
     - 是
     - 参考qosa_datacall_pdp_act_opt_e
     - 待获取的定时器的类型, 激活或去激活操作用的定时器

   * - pdp_timer
     - qosa_datacall_pdp_timer_t*
     - 是
     - 无
     - 定时器配置

qosa_datacall_pdp_timer_t结构体含义参考 :ref:`qosa_datacall_pdp_timer_t`

qosa_datacall_pdp_act_opt_e结构体含义参考 :ref:`qosa_datacall_pdp_act_opt_e`

- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值，参见 :ref:`qosa_datacall_errno_e` 章节。

- 使用注意事项

    无。