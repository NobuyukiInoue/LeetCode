defmodule Solution do
  # 227ms - 233ms
  @spec complex_number_multiply(num1 :: String.t, num2 :: String.t) :: String.t
  def complex_number_multiply(num1, num2) do
    flds1 = String.split(num1, "+")
    flds2 = String.split(num2, "+")

    n1r = String.to_integer(Enum.at(flds1, 0))
    temp = Enum.at(flds1, 1)
    n1i = String.to_integer(String.slice(temp, 0, String.length(temp) - 1))

    n2r = String.to_integer(Enum.at(flds2, 0))
    temp = Enum.at(flds2, 1)
    n2i = String.to_integer(String.slice(temp, 0, String.length(temp) - 1))

    re = n1r*n2r - n1i*n2i
    im = n1r*n2i + n1i*n2r
    Integer.to_string(re) <> "+" <> Integer.to_string(im) <> "i"
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "\"", "")
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")
    num1 = Enum.at(flds, 0)
    num2 = Enum.at(flds, 1)
    "num1 = \"" <> num1 <> "\", num2 = \"" <> num2 <> "\""|> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.complex_number_multiply(num1, num2)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
