defmodule Solution do
  # 266ms - 280ms
  @spec categorize_box(length :: integer, width :: integer, height :: integer, mass :: integer) :: String.t
  def categorize_box(length, width, height, mass) do
    bulky = Enum.max([length, width, height]) >= 10_000 or length*width*height >= 10_00_000_000
    heavy = mass >= 100
    cond do
      bulky and heavy ->
        "Both"
      bulky ->
        "Bulky"
      heavy ->
        "Heavy"
      true ->
        "Neither"
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    nums = for n <- String.split(flds, ",") do String.to_integer(n) end
    length = Enum.at(nums, 0)
    width = Enum.at(nums, 1)
    height = Enum.at(nums, 2)
    mass = Enum.at(nums, 3)
    "length = " <> Integer.to_string(length) <> ", width = " <> Integer.to_string(width) <> ", height = " <> Integer.to_string(height) <> ", mass = " <> Integer.to_string(mass) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.categorize_box(length, width, height, mass)
      "result = " <> result |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
