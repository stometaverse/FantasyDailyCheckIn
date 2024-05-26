# FantasyDailyCheckIn

Follow twitter account @stometaverse for updates 
关注推特 @stometaverse 会持续分享web3相关的信息！ 

# Instructions 

为了每日打卡，需要获得cookie 和 authorization的信息，authorization有效期非常短，cookie有效期要长很多
因此，1）先通过cookie生成authorization header 2）再发出daily checkin 的请求

要运行main.py 首先要拿到属于自己的一部分信息，下述细节哈 

## Step 1： 拿到cookie信息

1. logout当前账户
2. 在浏览器页面输入F12 打开console
3. 点击到network tab
4. 点击preserve log 
5. 搜索框输入authorize 
6. 在页面上完成用户登录
7. 找到authorize请求 
8. 在header栏当中找到对应的cookie  复制到AUTH_TOKEN_COOKIE处即可

![Screenshot 2024-05-26 at 13.14.45.png](..%2F..%2FDesktop%2FScreenshot%202024-05-26%20at%2013.14.45.png)

## Step 2. 拿到属于你的请求payload（为了动态生成authorization token）
1. 和第一步一样的窗口
2. 现在搜索privy
3. 找到请求，点击到Payload 
4. 选择copy object，把这一个对象粘贴到代码的PAYLOAD_FOR_AUTH_TOKEN

![Screenshot 2024-05-26 at 17.05.36.png](..%2F..%2FDesktop%2FScreenshot%202024-05-26%20at%2017.05.36.png)
## Step 3. 拿到你的钱包地址 
1. PAYLOAD_FOR_AUTH_TOKEN 当中包含你的钱包地址
2. 复制这个地址到PAYLOAD_FOR_DAILY_QUEST 的id 的部分即可

## Step 4. 运行代码

```
# 运行程序
python main.py 

# 如何有依赖确实的问题 
pip install xxx
```

# Suggestions 
1. 建议使用PM2 来对程序进行管理
2. 建议使用dotenv 来管理cookie 和token信息。 一定注意保护这两个信息，不要把这种关键且敏感的信息推到git repo上