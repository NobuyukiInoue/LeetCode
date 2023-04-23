defmodule Solution2 do
  # 229ms - 233ms
  @spec generate_parenthesis(n :: integer) :: [String.t]
  def generate_parenthesis(n) when n >= 1 and n <= 8 do
    n - 1
    |> generate_parenthesis(n)
    |> unnest_data("(")
    |> List.flatten()
  end

  def generate_parenthesis(0, 0) do
    {}
  end

  def generate_parenthesis(0, right_count) do
    {
      {")", generate_parenthesis(0, right_count - 1)}
    }
  end

  def generate_parenthesis(left_count, right_count) when left_count == right_count do
    {
      {"(", generate_parenthesis(left_count - 1, right_count)}
    }
  end

  def generate_parenthesis(left_count, right_count) when left_count < right_count do
    {
      {"(", generate_parenthesis(left_count - 1, right_count)},
      {")", generate_parenthesis(left_count, right_count - 1)}
    }
  end

  def unnest_data({}, prefix), do: prefix

  def unnest_data(data, prefix) when tuple_size(data) == 1 do
    element = elem(data, 0)
    [unnest_data(elem(element, 1), prefix <> elem(element, 0))]
  end

  def unnest_data(data, prefix) when tuple_size(data) == 2 do
    first_element = elem(data, 0)
    second_element = elem(data, 1)
    [unnest_data(elem(first_element, 1), prefix <> elem(first_element, 0)), unnest_data(elem(second_element, 1), prefix <> elem(second_element, 0))]
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    flds = String.replace(temp, "]", "")
    n = String.to_integer(flds)
    "n = " <> to_string(n) |> IO.puts()

    execright = Benchmark.measure(fn ->
      result = Solution.generate_parenthesis(n)
      "result = " <> Mylib.stringArray_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(execright, 3)) <> " [s]\n" |> IO.puts()
  end
end
