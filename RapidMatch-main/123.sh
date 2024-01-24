N=200  # 循环次数

for ((i=1; i<=N; i++))
do
    # 构建命令，注意$i的使用
    run_command="./RapidMatch.out -d ../../dataset/youtube/data_graph/youtube.graph -q ../../dataset/youtube/query_graph/query_dense_8_$i.graph -order nd -preprocess true -num MAX -time_limit 60 > output.txt"

    echo "Running command: $run_command"

    # 在这里执行命令，你可以取消下面这行的注释执行命令
    # eval $run_command
done
