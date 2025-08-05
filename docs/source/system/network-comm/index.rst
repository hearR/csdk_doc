========
datacall
========

--------------------
PDP概述
--------------------

PDP（Packet Data Protocol）是蜂窝网络中用于数据传输的基础协议，类似于传统互联网中的IP协议。它的主要作用是在蜂窝网络与外部数据网络（如互联网）之间建立数据连接通道。PDP通过定义连接的参数，确保数据可以顺利地从用户设备传输到网络和互联网。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1 PDP的基本概念
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PDP（包数据协议）是蜂窝网络中用于数据传输的一种协议。它负责设备与外部数据网络（如互联网、私有网络等）之间的数据连接。PDP的作用类似于传统互联网中的IP协议，通过管理和配置连接参数来确保数据在网络中的传输。PDP主要依赖于“PDP Context”，它是设备与网络之间协商数据传输的一组参数配置模板。

PDP包括以下几个基本要素：

1. PDP Context：配置数据连接所需的一组参数，定义了数据连接的具体行为。包括但不限于：

 - APN（接入点名称）

 - IP地址类型（如IPv4或IPv6）

 - 数据传输模式（如网络类型2G、3G、4G等）

2. PDP激活：设备连接到蜂窝网络后，通过PDP激活流程获取一个有效的IP地址。通过PDP协议，设备可以访问互联网或其他网络服务。

3. PDP地址：通过PDP激活过程，设备获得一个IP地址，这个IP地址将用于数据通信。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2 DataCall流程概述
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DataCall是指通信模块在蜂窝网络中建立数据连接的过程。这个过程主要是为了使设备能够通过运营商的蜂窝网络接入互联网或其他私有网络。DataCall流程中的核心任务是通过PDP激活来获取IP地址，并在设备与外部网络之间建立稳定的数据传输通道。

DataCall的流程通常包含以下几个步骤：

1. 设备接入运营商网络：

 - 设备通过蜂窝模块与运营商的网络连接，通常通过移动设备上的SIM卡认证，获得与运营商的网络连接。

2. PDP激活：

 - 设备向网络发送PDP激活请求，网络根据设备的请求配置PDP Context，并分配一个IP地址。PDP Context包括如APN、IP类型等连接信息。

 - 设备一旦成功激活PDP，就可以获取到IP地址。

3. 建立数据连接：

 - 设备使用获得的IP地址，通过TCP/IP等协议进行数据通信，能够访问互联网、传输数据或进行其他网络服务。

4. 数据传输：

 - 一旦建立了数据连接，设备就可以通过运营商的网络进行数据传输，支持各种应用如浏览网页、发送邮件、进行实时通信等。

5. 数据连接断开：

 - 当设备不再需要继续进行数据传输时，可以通过PDP去激活或删除PDP Context，断开数据连接。


简而言之，PDP协议通过定义网络连接的行为和参数，而DataCall流程通过PDP激活为设备提供了一个有效的网络连接，从而使设备能够进行数据传输。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DataCall 函数列表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: DataCall 函数列表
   :widths: 30 70
   :header-rows: 1

   * - 函数
     - 描述
   * - qosa_datacall_attach
     - 注册或者反注册网络
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

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_attach(qosa_uint8_t simid, qosa_uint8_t method, datacall_callback_cb_ptr cb, void* ctx)

- 功能描述

  注册或者反注册网络。设备只有在运营商网络注册成功之后，才可通过PDP的激活流程来获取运营商下发的IP地址。设备反注册成功网络之后，相当于在运营商网络中下线，同时设备之前获取到的IP地址也都会消失。

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

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.1.1 qosa_datacall_attach_stat_e
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: c

    typedef enum
    {
      QOSA_DATACALL_DETACH, 
      QOSA_DATACALL_ATTACH, 
    } qosa_datacall_attach_stat_e;

.. list-table:: qosa_datacall_attach_stat_e枚举值说明
   :header-rows: 1

   * - 枚举值
     - 说明
   * - QOSA_DATACALL_DETACH
     - 反注册网络
   * - QOSA_DATACALL_ATTACH
     - 注册网络


- 返回值说明

    函数执行成功返回 ``QOSA_DATACALL_OK``，否则返回其他qosa_datacall_errno_e枚举类型的枚举值。

.. _qosa_datacall_errno_e:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.1.2 qosa_datacall_errno_e
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

- 使用注意事项

    该函数为异步函数。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.2 qosa_datacall_wait_attached
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_bool_t qosa_datacall_wait_attached(qosa_uint8_t simid, qosa_uint32_t timeout)

- 功能描述

  执行时判断当前网络是否注册成功，如果当前没有注册成功，则会等待timeout的时间，如果这段时间内仍然没有注册成功，则返回false，如果期间注册网络成功，则会立即返回true。

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

  查询一个指定的PDP是否为已定义状态。已定义状态: 若用户侧配置了该PDP的PDP上下文参数、PDP鉴权参数、PDP QoS参数, 视为用户侧定义。

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
     - 1-15
     - PDP ID

- 返回值说明

    已定义返回 ``OSA_TRUE``，未定义返回 ``OSA_FALSE``。

- 使用注意事项

    无。


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.2 qosa_datacall_set_pdp_context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_set_pdp_context(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_pdp_context_t* pdp_ctx)

- 功能描述

  设置某个PDP ID的PDP context，用于定义数据连接的具体行为。

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
     - 1-15
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
     - 1-15
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

  获取特定PDP的PDP context。用来查询此PDP的IP TYPE，APN等信息。

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
     - 1-15
     - PDP ID

   * - pdp_ctx
     - qosa_pdp_context_t*
     - 是
     - 无
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
  PDP auth context，用于在建立数据连接时进行身份验证的一组参数。当设备通过蜂窝网络（如PPP拨号或IP连接）接入运营商网络时，可能需要向网络侧提供鉴权信息（如用户名和密码）以验证身份。

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
     - 1-15
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

  获取特定PDP的PDP auth context。用于查询此PDP用于鉴权的用户名、密码以及鉴权类型的鉴权配置。

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
     - 1-15
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

  此函数用于定义特定PDP的QoS profile。
  QoS profile是用于定义数据连接的服务质量（Quality of Service）的一组参数。它决定了数据传输的优先级、带宽、延迟、可靠性等关键指标，直接影响用户体验和业务质量。

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
     - 1-15
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

  此函数用于查询特定PDP的QoS profile.

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
     - 1-15
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
3 DNS的配置和查询
---------------------
DNS（域名系统，Domain Name System），用于将易记的域名（如 www.example.com）解析为计算机能够识别的 IP 地址（如 93.184.216.34）。
它是分布式、层级化的数据库系统，保证了海量主机名与 IP 地址之间的高效映射和查找。
一般情况下，模组注网成功时，核心网会下发DNS服务器的IP地址给模组，供模组用来解析域名，另外也支持自行配置期望的DNS服务器的IP地址。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3.1 qosa_datacall_get_dns_addr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qosa_datacall_errno_e qosa_datacall_get_dns_addr(qosa_uint8_t simid, qosa_uint8_t pdpid, qosa_datacall_dns_t* dns)

- 功能描述

  此函数用于获取某个PDP配置的dns服务器IP地址.

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
     - 1-15
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

  此函数用于设置dns服务器IP地址.

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
     - 1-15
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

  生成一个特定功能域的连接对象. 此对象可用于后续的数据拨号操作。如果参数非法, 将返回OSA_DATACALL_CONN_INVALID

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
     - 1-15
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

  获取特定datacall连接对象的连接状态.在应用侧使用一个特定的PDP连接前, 可以检查该状态, 如果其已经为连接状态, 表示该连接正在被使用

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

  获取特定datacall连接对象的详细信息.如果对应的连接对象没有激活, 将返回空的IP地址

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

-----------------------
示例 Demo 与流程图
-----------------------
datacall示例程序展示了QuecOS的datacall功能

.. image:: ../images/quecos-datacall-demo-workflow.png
   :align: center
   :alt: datacall demo流程图
   :figclass: align-center

.. code-block:: c

    #include "qosa_def.h"
    #include "qosa_log.h"

    #include "qosa_network.h"
    #include "qosa_datacall.h"
    #include "qosa_platform_cfg.h"
    #include "qosa_ip_addr.h"
    #include "qosa_event_notify.h"

    #define log_e(...)                                QOSA_LOG_E(LOG_TAG_MODEM, ##__VA_ARGS__)
    #define log_w(...)                                QOSA_LOG_W(LOG_TAG_MODEM, ##__VA_ARGS__)
    #define log_i(...)                                QOSA_LOG_I(LOG_TAG_MODEM, ##__VA_ARGS__)
    #define log_d(...)                                QOSA_LOG_D(LOG_TAG_MODEM, ##__VA_ARGS__)
    #define log_v(...)                                QOSA_LOG_V(LOG_TAG_MODEM, ##__VA_ARGS__)

    #define DATACALL_DEMO_WAIT_ATTACH_MAX_WAIT_TIME   300
    #define DATACALL_DEMO_WAIT_DATACALL_MAX_WAIT_TIME 120

    qosa_task_t g_datacall_demo_task = QOSA_NULL;
    qosa_msgq_t g_datacall_demo_msgq = QOSA_NULL;

    typedef enum
    {
        DATACALL_NW_DEACT_MSG,
    } datacall_demo_msg_e;

    typedef struct
    {
        datacall_demo_msg_e msgid; /**< datacall demo message type */
        void               *argv;
    } datacall_demo_msg_t;

    typedef struct
    {
        qosa_uint8_t simid; /**< SIM identification */
        qosa_uint8_t pdpid; /**< PDP identification */
    } datacall_demo_pdp_deact_ind_t;

    int datacall_nw_deact_pdp_cb(void *user_argv, void *argv)
    {
        QOSA_UNUSED(user_argv);

        datacall_demo_pdp_deact_ind_t *deact_ptr = QOSA_NULL;
        datacall_demo_msg_t            datacall_nw_deact_msg = {0};

        //get nw deact report params
        qosa_datacall_nw_deact_event_t *pdp_deatch_event = (qosa_datacall_nw_deact_event_t *)argv;

        log_i("enter,simid=%d,pdpid=%d", pdp_deatch_event->simid, pdp_deatch_event->pdpid);

        // melloc memory
        deact_ptr = (datacall_demo_pdp_deact_ind_t *)qosa_malloc(sizeof(datacall_demo_pdp_deact_ind_t));
        if (deact_ptr == QOSA_NULL)  // if melloc fail ,return
        {
            return 0;
        }

        deact_ptr->simid = pdp_deatch_event->simid;
        deact_ptr->pdpid = pdp_deatch_event->pdpid;

        // Preparing to send messages to the message queue
        datacall_nw_deact_msg.msgid = DATACALL_NW_DEACT_MSG;
        datacall_nw_deact_msg.argv = deact_ptr;

        qosa_msgq_release(g_datacall_demo_msgq, sizeof(datacall_demo_msg_t), (qosa_uint8_t *)&datacall_nw_deact_msg, QOSA_NO_WAIT);
        return 0;
    }

    static void datacall_demo_task(void *arg)
    {
        int                     ret = 0;
        int                     retry_count = 0;
        uint8_t                 simid = 0;
        int                     profile_idx = 1;
        qosa_datacall_conn_t    conn;
        qosa_bool_t             datacall_status = QOSA_FALSE;
        qosa_datacall_ip_info_t info = {0};
        datacall_demo_msg_t     datacall_task_msg = {0};
        qosa_pdp_context_t      pdp_ctx = {0};
        qosa_bool_t             is_attached = QOSA_FALSE;
        char                    ip4addr_buf[CONFIG_QOSA_INET_ADDRSTRLEN] = {0};
        char                    ip6addr_buf[CONFIG_QOSA_INET6_ADDRSTRLEN] = {0};

        //create message queue
        ret = qosa_msgq_create(&g_datacall_demo_msgq, sizeof(datacall_demo_msg_t), 20);
        log_i("create msgq result=%d", ret);

        qosa_task_sleep_sec(3);

        //if attach is successful before the maxtime timeout, it will immediately return QOSA_TRUE and enter second while loop
        //Otherwise, it will block until timeout and returning QOSA_FALSE and enter first while loop
        is_attached = qosa_datacall_wait_attached(simid, DATACALL_DEMO_WAIT_ATTACH_MAX_WAIT_TIME);
        if (!is_attached)
        {
            log_i("attach fail");
            goto exit;
        }

        //register network pdn deactive event callback
        qosa_event_notify_register(QOSA_EVENT_NW_PDN_DEACT, datacall_nw_deact_pdp_cb, QOSA_NULL);

        //config pdp context:APN, iptype
        //If the operator has restrictions on the APN during registration, needs to be set the APN provided by the operator
        const char *apn_str = "test";
        pdp_ctx.apn_valid = QOSA_TRUE;
        pdp_ctx.pdp_type = QOSA_PDP_TYPE_IP;  //ipv4
        if (pdp_ctx.apn_valid)
        {
            qosa_memcpy(pdp_ctx.apn, apn_str, qosa_strlen(apn_str));
        }

        ret = qosa_datacall_set_pdp_context(simid, profile_idx, &pdp_ctx);
        log_i("set pdp context, ret=%d", ret);

        //create datacall object
        conn = qosa_datacall_conn_new(simid, profile_idx, QOSA_DATACALL_CONN_TCPIP);

        //start excute datacall(sync)
        ret = qosa_datacall_start(conn, DATACALL_DEMO_WAIT_DATACALL_MAX_WAIT_TIME);
        if (ret != QOSA_DATACALL_OK)
        {
            log_i("datacall fail ,ret=%d", ret);
            goto exit;
        }

        //get datacall status(0: deactive 1:active)
        datacall_status = qosa_datacall_get_status(conn);
        log_i("datacall status=%d", datacall_status);

        //get ip info from datacall
        ret = qosa_datacall_get_ip_info(conn, &info);
        log_i("pdpid=%d,simid=%d", info.simcid.pdpid, info.simcid.simid);
        log_i("ip_type=%d", info.ip_type);

        if (info.ip_type == QOSA_PDP_IPV4)
        {
            //ipv4 info
            qosa_memset(ip4addr_buf, 0, sizeof(ip4addr_buf));
            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET, &info.ipv4_ip.addr.ipv4_addr, ip4addr_buf, sizeof(ip4addr_buf));
            log_i("ipv4 addr:%s", ip4addr_buf);
        }
        else if (info.ip_type == QOSA_PDP_IPV6)
        {
            //ipv6 info
            qosa_memset(ip6addr_buf, 0, sizeof(ip6addr_buf));
            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET6, &info.ipv6_ip.addr.ipv6_addr, ip6addr_buf, sizeof(ip6addr_buf));
            log_i("ipv6 addr:%s", ip6addr_buf);
        }
        else
        {
            //ipv4 and ipv6 info
            qosa_memset(ip4addr_buf, 0, sizeof(ip4addr_buf));
            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET, &info.ipv4_ip.addr.ipv4_addr, ip4addr_buf, sizeof(ip4addr_buf));
            log_i("ipv4 addr:%s", ip4addr_buf);
            qosa_memset(ip6addr_buf, 0, sizeof(ip6addr_buf));
            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET6, &info.ipv6_ip.addr.ipv6_addr, ip6addr_buf, sizeof(ip6addr_buf));
            log_i("ipv6 addr:%s", ip6addr_buf);
        }

        while (1)
        {
            ret = qosa_msgq_wait(g_datacall_demo_msgq, (qosa_uint8_t *)&datacall_task_msg, sizeof(datacall_demo_msg_t), QOSA_WAIT_FOREVER);
            if (ret != 0)
                continue;
            log_i("enter datacall demo task, msgid=%d", datacall_task_msg.msgid);

            switch (datacall_task_msg.msgid)
            {
                case DATACALL_NW_DEACT_MSG: {
                    qosa_datacall_nw_deact_event_t *pdp_deatch_event = (qosa_datacall_nw_deact_event_t *)datacall_task_msg.argv;
                    log_i("simid=%d,deact pdpid=%d", pdp_deatch_event->simid, pdp_deatch_event->pdpid);

                    //Try reactive 10 times, time interval is 20 seconds
                    while (((ret = qosa_datacall_start(conn, DATACALL_DEMO_WAIT_DATACALL_MAX_WAIT_TIME)) != QOSA_DATACALL_OK) && (retry_count < 10))
                    {
                        retry_count++;
                        log_i("datacall fail, the retry count is %d", retry_count);
                        qosa_task_sleep_sec(20);
                    }

                    if (ret == QOSA_DATACALL_OK)
                    {
                        retry_count = 0;

                        //get datacall status(0: deactive 1:active)
                        datacall_status = qosa_datacall_get_status(conn);
                        log_i("datacall status=%d", datacall_status);
                        //get ip info from datacall
                        ret = qosa_datacall_get_ip_info(conn, &info);
                        log_i("pdpid=%d,simid=%d", info.simcid.pdpid, info.simcid.simid);
                        log_i("ip type=%d", info.ip_type);

                        char ip4addr_buf[CONFIG_QOSA_INET_ADDRSTRLEN] = {0};
                        char ip6addr_buf[CONFIG_QOSA_INET6_ADDRSTRLEN] = {0};

                        if (info.ip_type == QOSA_PDP_IPV4)
                        {
                            qosa_memset(ip4addr_buf, 0, sizeof(ip4addr_buf));
                            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET, &info.ipv4_ip.addr.ipv4_addr, ip4addr_buf, sizeof(ip4addr_buf));
                            log_i("ipv4 addr:%s", ip4addr_buf);
                        }
                        else if (info.ip_type == QOSA_PDP_IPV6)
                        {
                            qosa_memset(ip6addr_buf, 0, sizeof(ip6addr_buf));
                            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET6, &info.ipv6_ip.addr.ipv6_addr, ip6addr_buf, sizeof(ip6addr_buf));
                            log_i("ipv6 addr:%s", ip6addr_buf);
                        }
                        else
                        {
                            qosa_memset(ip4addr_buf, 0, sizeof(ip4addr_buf));
                            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET, &info.ipv4_ip.addr.ipv4_addr, ip4addr_buf, sizeof(ip4addr_buf));
                            log_i("ipv4 addr:%s", ip4addr_buf);
                            qosa_memset(ip6addr_buf, 0, sizeof(ip6addr_buf));
                            qosa_ip_addr_inet_ntop(QOSA_IP_ADDR_AF_INET6, &info.ipv6_ip.addr.ipv6_addr, ip6addr_buf, sizeof(ip6addr_buf));
                            log_i("ipv6 addr:%s", ip6addr_buf);
                        }
                    }
                    else
                    {
                        log_i("datacall fail in nw deact pdn event");
                    }
                    qosa_free(datacall_task_msg.argv);
                }
                break;

                default:
                    break;
            }
        }

    exit:
        //unregister network pdn deactive event callback
        qosa_event_notify_unregister(QOSA_EVENT_NW_PDN_DEACT, datacall_nw_deact_pdp_cb);

        //delete msgqueue and task
        qosa_msgq_delete(g_datacall_demo_msgq);
        qosa_task_delete(g_datacall_demo_task);
    }

    void datacall_demo_init(void)
    {
        int err = 0;
        //create datacall demo main task
        err = qosa_task_create(&g_datacall_demo_task, 4 * 1024, QOSA_PRIORITY_NORMAL, "QDATACALLDEMO", datacall_demo_task, QOSA_NULL);

        if (err != QOSA_OK)
        {
            log_d("datacall_demo task create error");
            return;
        }
    }

说明：
1. 创建消息队列  
2. 阻塞等待注网成功  
3. 注册网络事件的回调函数  
4. 配置pdp context  
5. 创建datacall对象  
6. 开始datacall  
7. 获取当前的datacall对象的状态是否成功  
8. 获取当前的datacall对象获取的IP信息  
9. 阻塞task，如果网络去激活pdp事件触发，则会发送网络去激活pdp的消息到task中  
10. 重试datacall激活流程直到成功，最大次数10次  
11. 如果datacall成功，则获取当前的datacall对象的状态和获取的IP信息  
12. 回到9  


