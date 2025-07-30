========
NTP
========

NTP实现网络时间协议客户端功能，通过与NTP服务器交互校准设备时钟。

此模块包含了客户端会话管理，异步时间同步，网络自适应和双栈支持等功能。



.. list-table:: NTP 函数列表
   :widths: 30 70
   :header-rows: 1

   * - 函数
     - 描述 
   * - qcm_ntp_client_new 
     - 初始化NTP请求，并获取对应ntp操作句柄 
   * - qcm_ntp_client_free 
     - ntp 释放函数,实际释放在ntp完成后会自动执行
   * - qcm_ntp_sync_start 
     - ntp 异步请求动作

---------------------------
1 NTP客户端创建和释放
---------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.1 qcm_ntp_client_new
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qcm_ntp_client_id qcm_ntp_client_new(void)

- 功能描述
    初始化NTP请求，并获取对应ntp操作句柄。

- 参数说明
    无参数传入。

- 返回值说明

    函数执行成功返回 ``client id 大于0``，失败返回-1。

- 使用注意事项

    资源在ntp的回调函数中通知后会自动释放，无法管理。

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.2 qcm_ntp_client_free
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qcm_ntp_result_code qcm_ntp_client_free(qcm_ntp_client_id client_id)

- 功能描述
    ntp 释放函数,实际释放在ntp完成后会自动执行

- 参数说明

.. list-table:: qcm_ntp_client_free参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - client_id
     - qcm_ntp_client_id
     - 是
     - -1，1，2，3
     - 对应客户端句柄ID

- 返回值说明

    函数执行成功返回 ``QCM_NTP_SUCCESS``，失败返回其他值。

- 使用注意事项

    此处为方便api成对，实际释放在ntp完成后会自动执行。
	
-----------------------------
2 NTP时间同步控制接口
-----------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2.1 qcm_ntp_sync_start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- 函数原型

.. code-block:: c

    qcm_ntp_result_code qcm_ntp_sync_start(
		qcm_ntp_client_id      client_id,
		const char            *host_name,
		qosa_uint16_t          host_port,
		qcm_ntp_config_t      *ntp_options,
		qcm_ntp_sync_result_cb cb_fun,
		void                  *user_param
    )

- 功能描述
    ntp 异步请求动作。

- 参数说明

.. list-table:: qcm_ntp_sync_start参数
   :header-rows: 1

   * - 参数名
     - 类型
     - 是否必填
     - 范围/单位
     - 说明

   * - client_id
     - qcm_ntp_client_id
     - 是
     - 1-3
     - 对应从qcm_ntp_client_new 函数中获取到的ntp client id

   * - host_name
     - const char*
     - 是
     - 最大128字节
     - 对应host 域名或IP地址

   * - host_port
     - qosa_uint16_t
     - 是
     - 1-65535
     - 对应NTP 服务器端口，一般默认为123
	 
   * - ntp_options
     - qcm_ntp_config_t*
     - 是
     - 参考qcm_ntp_config_t*
     - 对应用户配置的参数
	 
   * - cb_fun
     - qcm_ntp_sync_result_cb
     - 是
     - 参考qcm_ntp_sync_result_cb
     - 对应结果返回cb函数
	 	 
   * - user_param
     - void*
     - 是
     - 无
     - 用户携带的参数
	 
qcm_ntp_config_t枚举值

.. code:: c

   typedef struct 
   {
		qosa_uint8_t  sim_id;            
		qosa_uint8_t  pdp_id;            
		qosa_uint32_t num_data_bytes;    
		qosa_bool_t   sync_local_time;   
		qosa_uint8_t  retry_cnt;         
		qosa_uint16_t retry_interval_tm; 
   } qcm_ntp_config_t;
   
.. list-table:: NTP qcm_ntp_config_t枚举值说明
   :header-rows: 1

   * - 枚举值
     - 说明
   * - sim_id
     - 对应sim卡的ID序号
   * - pdp_id
     - 对应pdp激活场景的序号
   * - num_data_bytes
     - ntp 发送数据包的长度
   * - sync_local_time
     - 是否自动将同步时间设置为本地时间
   * - retry_cnt
     - NTP数据发送重试次数
   * - retry_interval_tm
     - NTP数据发送重试间隔时间
	 
qcm_ntp_sync_result_cb枚举值

.. code:: c

   typedef void (*qcm_ntp_sync_result_cb)
   (
		qcm_ntp_client_id client_id, 
		qcm_ntp_result_code result, 
		qosa_rtc_time_t *sync_time, 
		void *arg            
   );

.. list-table:: NTP qcm_ntp_sync_result_cb枚举值说明
   :header-rows: 1

   * - 枚举值
     - 说明
   * - qcm_ntp_client_id
     - 对应客户端句柄ID
   * - qcm_ntp_result_code
     - NTP完成结果
   * - qosa_rtc_time_t*
     - 记录NTP执行成功的结果
   * - void*
     - 用户传入的用户参数
	 
- 返回值说明

    函数执行成功返回 ``QCM_NTP_SUCCESS``，失败返回其他值。

- 使用注意事项

    无。
	
