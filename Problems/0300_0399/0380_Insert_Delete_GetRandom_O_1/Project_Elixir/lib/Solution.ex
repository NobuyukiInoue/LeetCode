defmodule Solution do
  # 329ms - 357ms
  @spec sol(cmds :: [String.t], args :: [[integer]]) :: [String.t]
  def sol(cmds, args) do
    Enum.zip_reduce(cmds, args, [], fn cmd, arg, res ->
      case cmd do
        "RandomizedSet" ->
          RandomizedSet.init_()
          ["null" | res]
        "insert" ->
          [(RandomizedSet.insert(arg |> hd) |> to_string()) | res]
        "remove" ->
          [(RandomizedSet.remove(arg |> hd) |> to_string()) | res]
        "getRandom" ->
          [(RandomizedSet.get_random() |> to_string()) | res]
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
          [arg |> String.replace("[",  "") |> String.replace("]", "") |> String.to_integer()]
        else
          []
        end
      end

      "cmds = " <> Mylib.stringArray_to_string(cmds) <> ", args = [" <> Mylib.intIntList_to_string(args) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.sol(cmds, args)
      "result = [" <> Mylib.stringArray_to_string(result) <> "]" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
