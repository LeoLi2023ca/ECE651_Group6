#!/bin/bash

# 定义变量
EC2_HOST="ec2-user@18.219.51.210"
APP_NAME="next_app"
KEY_PATH="ECE651_Group6/Front-end Code/next_app/front-end.pem"
APP_DIR="ECE651_Group6/Front-end Code/next_app"  # 指向 Git 仓库中的应用目录
DIST_FOLDER="$APP_DIR/.next"  # 构建目录
REMOTE_APP_PATH="/home/ec2-user/$APP_NAME"  # 远程EC2上的应用路径

# 进入应用目录
echo "Entering the application directory..."
cd $APP_DIR

# 打包应用
echo "Packing the application..."
zip -r $APP_NAME.zip $DIST_FOLDER package.json yarn.lock

# 返回到原始目录 (可选)
cd -

# 上传到 EC2
echo "Uploading to EC2 instance..."
scp -i $KEY_PATH $APP_NAME.zip $EC2_HOST:$REMOTE_APP_PATH

# 远程执行部署命令
echo "Deploying on EC2 instance..."
ssh -i $KEY_PATH $EC2_HOST << EOF
  cd $REMOTE_APP_PATH
  unzip -o $APP_NAME.zip
  yarn install --production
  pm2 restart all
EOF

echo "Deployment completed."
