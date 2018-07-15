# Deployment
### Backend
```
$git clone https://github.com/ProgressOfSAD/Backend.git
$cd Backend
$./deploy.sh
```
说明：需要docker环境，同时，需要进入'./Backend/web_server/web_server/settings.py'文件中，找到  
```
DOMAIN = 'http://172.18.158.55:80'
```
将DOMAIN的IP改成执行当前代码的服务器的IP地址以及端口号

### Frontend
1. 从GitHub上clone项目
```
$git clone https://github.com/ProgressOfSAD/Frontend.git
```

2. 获取后台部署所在的主机IP。

3. 进入'/Frontend/user/config/index.js'文件，找到
```
proxyTable: {
      '/api': {
        target: 'http://172.18.158.55',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/'
        }
      }
    }
```
将target的IP改成后台的IP（如果指定了端口则加上端口号）

4. 同理，进入'/Frontend/admin/config/ndex.js'文件，找到
```
'/server': {    //将www.exaple.com印射为/apis
        target: 'http://172.18.158.55',
        //target: 'http://193.112.160.232:8010',  // 接口域名
        changeOrigin: true,  //是否跨域
        pathRewrite: {
            '^/server': ''   //需要rewrite的,
        }   
```
将target的IP改成后台的IP（如果指定了端口则加上端口号）

5. 回到项目根目录，运行部署脚本

```
$cd Frontend
$./deploy.sh
```
说明：需要docker环境
