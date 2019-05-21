DROP TABLE IF EXISTS `bigdata_queue`;
CREATE TABLE `bigdata_queue` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` tinyint(2) NOT NULL COMMENT '类型',
  `is_work` tinyint(255) NOT NULL DEFAULT '0' COMMENT '是否为工作状态',
  `action` varchar(2000) CHARACTER SET utf8mb4 NOT NULL COMMENT '队列动作',
  `params` text CHARACTER SET utf8mb4 COMMENT '参数预留',
  `fail_ip` varchar(20) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '任务失败机器的IP',
  `fail_times` int(5) NOT NULL DEFAULT '0' COMMENT '任务失败的次数',
  `create_times` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  KEY `type` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


DROP TABLE IF EXISTS `bigdata_web_seed`;
CREATE TABLE `bigdata_web_seed` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(2000) NOT NULL COMMENT '种子URL',
  `md5` varchar(40) NOT NULL COMMENT '种子URL的MD5',
  `domain` varchar(100) NOT NULL COMMENT '种子网站的domain',
  `host` varchar(200) NOT NULL COMMENT '种子网站HOST',
  `category` varchar(200) NOT NULL COMMENT '分类',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `last_crawl_time` timestamp NULL DEFAULT NULL COMMENT '种子最后成功爬取时间',
  `last_crawl_internally` int(10) DEFAULT NULL COMMENT '种子最后成功爬取内链数',
  `last_crawl_externally` int(10) DEFAULT NULL COMMENT '种子最后成功爬取外链数',
  `fail_times` int(11) DEFAULT '0' COMMENT '抓取失败次数',
  `fail_ip` varchar(20) DEFAULT NULL COMMENT '最后失败的机器IP',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '状态 0 启用 1 关闭',
  PRIMARY KEY (`md5`),
  KEY `id` (`id`) USING BTREE,
  KEY `host` (`host`(191)) USING BTREE,
  KEY `domain` (`domain`) USING BTREE,
  KEY `md5` (`md5`) USING BTREE,
  KEY `status` (`status`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;


DROP TABLE IF EXISTS `bigdata_web_seed_internally`;
CREATE TABLE `bigdata_web_seed_internally` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(2000) NOT NULL COMMENT '种子URL',
  `md5` varchar(40) NOT NULL COMMENT '种子URL的MD5',
  `param` text COMMENT '参数预留',
  `domain` varchar(100) NOT NULL COMMENT '种子网站的domain',
  `host` varchar(200) NOT NULL COMMENT '种子网站HOST',
  `a_url` varchar(2000) NOT NULL COMMENT '抓取页中的内链',
  `a_md5` varchar(40) NOT NULL COMMENT '抓取页中的内链的MD5',
  `a_host` varchar(200) NOT NULL COMMENT '抓取页中的内链的HOST',
  `a_xpath` text NOT NULL COMMENT '抓取页中的内链的XPATH',
  `a_title` text COMMENT '抓取页中的内链的title',
  `create_time` int(11) NOT NULL COMMENT '记录创建时间',
  `create_day` int(11) NOT NULL COMMENT '记录创建天',
  `create_hour` int(11) NOT NULL COMMENT '记录创建小时',
  `update_time` int(11) NOT NULL COMMENT '记录更新时间',
  `fail_times` int(11) DEFAULT '0' COMMENT '抓取失败次数',
  `fail_ip` varchar(20) DEFAULT NULL COMMENT '最后失败的机器IP',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '下载状态 0 未处理 1 已处理',
  PRIMARY KEY (`md5`,`a_md5`),
  KEY `id` (`id`) USING BTREE,
  KEY `host` (`host`(191)) USING BTREE,
  KEY `domain` (`domain`) USING BTREE,
  KEY `md5` (`md5`) USING BTREE,
  KEY `a_md5` (`a_md5`) USING BTREE,
  KEY `md5_aMd5` (`md5`,`a_md5`) USING BTREE,
  KEY `a_host` (`a_host`(191)) USING BTREE,
  KEY `status` (`status`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;


DROP TABLE IF EXISTS `bigdata_web_seed_externally`;
CREATE TABLE `bigdata_web_seed_externally` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(2000) NOT NULL COMMENT '种子URL',
  `md5` varchar(40) NOT NULL COMMENT '种子URL的MD5',
  `param` text COMMENT '参数预留',
  `domain` varchar(100) NOT NULL COMMENT '种子网站的domain',
  `host` varchar(200) NOT NULL COMMENT '种子网站HOST',
  `a_url` varchar(2000) NOT NULL COMMENT '抓取页中的外链',
  `a_md5` varchar(40) NOT NULL COMMENT '抓取页中的外链的MD5',
  `a_host` varchar(200) NOT NULL COMMENT '抓取页中的外链的HOST',
  `a_xpath` text NOT NULL COMMENT '抓取页中的外链的XPATH',
  `a_title` text COMMENT '抓取页中的外链的title',
  `create_time` int(11) NOT NULL COMMENT '记录创建时间',
  `create_day` int(11) NOT NULL COMMENT '记录创建天',
  `create_hour` int(11) NOT NULL COMMENT '记录创建小时',
  `update_time` int(11) NOT NULL COMMENT '记录更新时间',
  `fail_times` int(11) DEFAULT '0' COMMENT '抓取失败次数',
  `fail_ip` varchar(20) DEFAULT NULL COMMENT '最后失败的机器IP',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '下载状态 0 未处理 1 已处理',
  PRIMARY KEY (`md5`,`a_md5`),
  KEY `id` (`id`) USING BTREE,
  KEY `host` (`host`(191)) USING BTREE,
  KEY `domain` (`domain`) USING BTREE,
  KEY `md5` (`md5`) USING BTREE,
  KEY `a_md5` (`a_md5`) USING BTREE,
  KEY `md5_aMd5` (`md5`,`a_md5`) USING BTREE,
  KEY `a_host` (`a_host`(191)) USING BTREE,
  KEY `status` (`status`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;


DROP TABLE IF EXISTS `bigdata_web_page`;
CREATE TABLE `bigdata_web_page` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `url` varchar(2000) NOT NULL DEFAULT '' COMMENT '网页URL',
  `md5` varchar(40) NOT NULL COMMENT 'URL的MD5值',
  `param` text COMMENT '参数预留',
  `domain` varchar(100) NOT NULL COMMENT '网站domain',
  `host` varchar(200) NOT NULL COMMENT '网站HOST',
  `title` varchar(500) DEFAULT NULL COMMENT '网页的title标签内容',
  `create_time` int(11) NOT NULL COMMENT '记录创建时间',
  `create_day` int(11) NOT NULL COMMENT '记录创建天',
  `create_hour` int(11) NOT NULL COMMENT '记录创建小时',
  `update_time` int(11) NOT NULL COMMENT '记录更新时间',
  `fail_times` int(11) DEFAULT '0' COMMENT '抓取失败次数',
  `fail_ip` varchar(20) DEFAULT NULL COMMENT '最后失败的机器IP',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否成功下载 1 成功 2 未成功',
  PRIMARY KEY (`md5`),
  KEY `id` (`id`),
  KEY `host` (`host`(191)),
  KEY `update_time` (`update_time`),
  KEY `md5` (`md5`),
  KEY `domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;




#on DUPLICATE KEY 的SQL例子
insert_web_page_sql = """
    insert into bigdata_web_page (url,md5,create_time,create_day,create_hour,domain,param,update_time,host,
    title,fail_ip,status) values ("%s","%s",%s,%s,%s,"%s","%s",%s,"%s","%s","%s",%s)
    on DUPLICATE KEY UPDATE fail_times=fail_times+1,fail_ip=values(fail_ip);
"""