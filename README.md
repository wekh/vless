## 一：CF Vless节点可自定义内容

#### 可修改Cloudflare_vless文件下的_worker.js文件

1、UUID必须自定义

2、如果无法访问CF类网站或者ChatGPT，说明ProxyIP失效，可更换ProxyIP，自定义

3、伪装网页目前留空，显示为400 Bad Request界面，可自定义

#### 也可在CF-workers/pages界面中使用变量设置，注：变量设置结果将覆盖本地修改结果
| 变量作用 | 变量名称 | 变量默认值 |
| :--- | :--- | :--- |
| 1、必要的UUID | UUID |cfd42f8b-2e58-4e4c-94f1-253e935b53ac|
| 2、能上CF类网站 | PROXYIP |proxyip.fxxk.dedyn.io|
| 3、优选域名 | ADD |优选域名|
| 4、优选订阅地址 | SUB |vless.fxxk.dedyn.io|

---------------------------------

## 二：查看相关分享链接（单节点，非订阅）
#### CF Vless分享链接，在网页输入：(workers/pages/自定义)域名/自定义uuid

注意： 由于workers域名已被全网TLS阻断、pages域名已被中国移动TLS阻断

所以需使用自定义域名或者在代理环境下才可查看分享链接，了解CF-workers/pages节点的特点，可手搓无数个节点


