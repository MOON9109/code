aws configure --profile [profile_새이름]

# AWS Access Key ID, AWS Secret Access Key, Default region name , Default output format 입력하라고 나온다


aws configure --profile [설정한 이름 ]
#설정한 정보들이 나온다.


#기존 shell script에 profile 추가하면 된다.
docker build --platform=linux/amd64 -t [container] .
aws ecr get-login-password --profile [설정한 이름] --region [지역] | docker login --username AWS --password-stdin [사용자 숫자 이름].dkr.ecr.[지역].amazonaws.com/[ecr_repo]

docker tag [container]:latest [사용자 숫자 이름].dkr.ecr.[지역].amazonaws.com/[ecr_repo]:latest
docker push [사용자 숫자 이름].dkr.ecr.[지역].amazonaws.com/[ecr_repo]