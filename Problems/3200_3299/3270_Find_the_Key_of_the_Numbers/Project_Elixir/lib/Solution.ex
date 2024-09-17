defmodule Solution do
  # 286ms - 357ms
  @spec generate_key(num1 :: integer, num2 :: integer, num3 :: integer) :: integer
  def generate_key(num1, num2, num3) do
    generate_key(num1, num2, num3, 10, 0)
  end

  @spec generate_key(num1 :: integer, num2 :: integer, num3 :: integer, dv :: integer, ans :: integer) :: integer
  def generate_key(num1, num2, num3, dv, ans) when dv < 100000 do
    d1= rem(num1, dv)
    d2 = rem(num2, dv)
    d3 = rem(num3, dv)
    generate_key(num1 - d1, num2 - d2, num3 - d3, dv*10, ans + Enum.min([d1, d2, d3]))
  end

  def generate_key(_num1, _num2, _num3, _dv, ans) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    num1 = String.to_integer(Enum.at(flds, 0))
    num2 = String.to_integer(Enum.at(flds, 1))
    num3 = String.to_integer(Enum.at(flds, 2))
    "num1 = " <> Integer.to_string(num1) <> ", num2 = " <> Integer.to_string(num2) <> ", num3 = " <> Integer.to_string(num3) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.generate_key(num1, num2, num3)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
