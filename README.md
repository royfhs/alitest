# alitest
For 2019 alitest 1st round test

Intro :<br>
- 微服务服务器端，提供一个http服务，实现因式分解
- 接受参数范围为2~2147483647

Clone && Build :<br>
- `git clone https://github.com/royfhs/alitest.git && cd ./alitest`
- `docker build -t alitest .`
- `docker run -P alitest` （需要通过docker ps查看所开放的随机端口，随后进行访问）
- or `docker run -p xxxx:5000 alitest` (xxxx为欲开放宿主机端口，如8080)

Usage :
- 指定xxxx端口或通过`docker ps`查看映射的随机端口
- `curl localhost:xxxx/factors?number=<int>`（xxxx为端口号，`<int>`接受参数范围为2~2147483647）

Example :<br>
\# `curl localhost:32770/factors?number=217896473`<br>
`{ "result": "151*1051*1373" }`<br><br>

PS :<br>
若使用`ZSH`，需要在`curl`命令中的`?`前加转义符号
