docker run -d \
--name chat_auth_bot \
-v `pwd`/config.yaml:/root/chatAuthBot/config.yaml \
--network host \
ccr.ccs.tencentyun.com/chaos_private/chat_auth_bot
