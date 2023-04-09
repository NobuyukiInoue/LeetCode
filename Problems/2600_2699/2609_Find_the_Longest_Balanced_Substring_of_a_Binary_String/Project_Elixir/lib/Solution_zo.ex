defmodule Solution_zo do
  # 639ms - 727ms
  @spec find_the_longest_balanced_substring(s :: String.t) :: integer
  def find_the_longest_balanced_substring(s) do
    find_the_longest_balanced_substring(s, 0, 0)
  end

  @spec find_the_longest_balanced_substring(s :: String.t, res :: integer, i :: integer) :: integer
  def find_the_longest_balanced_substring(s, res, i) do
#   "res = " <> Integer.to_string(res) <> ", i = " <> Integer.to_string(i) <> ", z = " <> Integer.to_string(z) <> ", o = " <> Integer.to_string(o) |> IO.puts()
#   "res = " <> Integer.to_string(res) <> ", i = " <> Integer.to_string(i) |> IO.puts()
    if i >= String.length(s) do
      res
    else
      {i1, z1} = step_z(s, i, 0)
      {i2, res2} = step_o(s, res, i1, z1, 0)
      i3 = step_i(s, res2, i2)
      find_the_longest_balanced_substring(s, res2, i3)
    end
  end

  @spec step_z(s :: String.t, i :: integer, z :: integer) :: {i ::integer, z :: integer}
  def step_z(s, i, z) do
    if i < String.length(s) and String.at(s, i) == "0" do
      step_z(s, i + 1, z + 1)
    else
      {i, z}
    end
  end

  @spec step_o(s :: String.t, res :: integer, i :: integer, z :: integer, o :: integer) :: {i ::integer, res :: integer}
  def step_o(s, res, i, z, o) do
    if i < String.length(s) and String.at(s, i) == "1" and z > o do
      step_o(s, max(res, (o + 1)*2) , i + 1, z, o + 1)
    else
      {i, res}
    end
  end

  @spec step_i(s :: String.t, res :: integer, i :: integer) :: integer
  def step_i(s, res, i) do
    if i < String.length(s) and String.at(s, i) == "1" do
      step_i(s, res, i + 1)
    else
      i
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    temp = String.replace(temp, "\"", "")
    s = String.replace(temp, ", ", ",")
    "s = " <> s |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.find_the_longest_balanced_substring(s)
      "result = " <> to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
