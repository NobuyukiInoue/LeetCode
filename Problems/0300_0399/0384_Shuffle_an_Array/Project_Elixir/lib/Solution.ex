defmodule Solution do
  # 329ms - 357ms
  @spec sol(cmds :: [String.t], args :: [[integer]]) :: [[integer]]
  def sol(cmds, args) do
    Enum.zip_reduce(cmds, args, [], fn cmd, arg, res ->
      case cmd do
        "Solution" ->
          Solution2.init_(arg)
          [arg | res]
        "reset" ->
          [Solution2.reset() | res]
        "shuffle" ->
          [Solution2.shuffle() | res]
        _ ->
          [[] | res]
      end
    end) |> Enum.reverse()
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    flds = temp |> String.replace("\"", "") |> String.replace(", ", ",") |> String.split("],[[")

    cmds = Enum.at(flds, 0) |> String.replace("[", "") |> String.split(",")

    args_str = Enum.at(flds, 1) |> String.replace("]]]", "") |> String.split("],[")
    args =
      for arg <- args_str do
        if arg != "" do
          arg = arg |> String.replace("[",  "") |> String.replace("]", "")
          for n <- String.split(arg, ",") do
            String.to_integer(n)
          end
        else
          []
        end
      end

      "cmds = " <> Mylib.stringArray_to_string(cmds) <> ", args = [" <> Mylib.intIntList_to_string(args) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sol(cmds, args)
      "result = [" <> Mylib.intIntList_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
