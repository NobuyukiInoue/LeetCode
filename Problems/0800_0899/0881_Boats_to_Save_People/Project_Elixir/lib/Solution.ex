defmodule Solution do
  # 417ms - 490ms
  @spec num_rescue_boats(people :: [integer], limit :: integer) :: integer
  def num_rescue_boats(people, limit) do
    people = Enum.sort(people)
    count(people, Enum.reverse(people), length(people), limit, 0)
  end

  @spec count(list1 :: [integer], list2 :: [integer], n :: integer, limit :: integer, ans :: integer) :: integer
  def count([light | list1], [heavy | list2], n, limit, ans) when light + heavy > limit do
    count([light | list1], list2, n - 1, limit, ans + 1)
  end

  def count([_light | list1], [_heavy | list2], n, limit, ans) when n >= 2 do
    count(list1, list2, n - 2, limit, ans + 1)
  end

  def count(_list1, _list2, n, _limit, ans) do
    ans + n
  end

  # 602ms - 669ms
  @spec num_rescue_boats2(people :: [integer], limit :: integer) :: integer
  def num_rescue_boats2(people, limit) do
    {_, m_people} =
      people
      |> Enum.sort()
      |> Enum.reduce({0, %{}}, fn weight, {i, m_people} ->
        {i + 1, Map.put(m_people, i, weight)}
      end)
    count(0, Enum.count(people) - 1, limit, m_people, 0)
  end

  @spec count2(i :: integer, j :: integer, limit :: integer, m_people :: %{}, ans :: integer) :: integer
  def count2(i, j, limit, m_people, ans) when i <= j do
    if m_people[i] + m_people[j] <= limit do
      count2(i + 1, j - 1, limit, m_people, ans + 1)
    else
      count2(i, j - 1, limit, m_people, ans + 1)
    end
  end

  def count2(_i, _j, _limit, _m_people, ans) do
    ans
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    people =
      for num <- String.split(Enum.at(flds, 0), ",") do
          String.to_integer(num)
      end

    limit = String.to_integer(Enum.at(flds, 1))

    "people = " <> Mylib.intList_to_string(people) <> ", limit = " <> Integer.to_string(limit) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.num_rescue_boats(people, limit)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
