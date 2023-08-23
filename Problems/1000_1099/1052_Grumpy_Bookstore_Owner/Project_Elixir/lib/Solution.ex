defmodule Solution do
  # 2376ms - 2462ms
  @spec max_satisfied(customers :: [integer], grumpy :: [integer], minutes :: integer) :: integer
  def max_satisfied(customers, grumpy, minutes) do
    {_, total, grumpy} =
      Enum.reduce(customers, {0, 0, []}, fn customers_i, {i, total, n_grumpy} ->
        grumpy_i = Enum.at(grumpy, i)
        {i + 1, total + customers_i*(1 - grumpy_i), [customers_i*grumpy_i | n_grumpy]}
      end)
      grumpy = Enum.reverse(grumpy)
    {_, _, m_customers} =
      Enum.reduce(grumpy, {0, 0, 0}, fn grumpy_i, {i, save, m_customers} ->
        if i < minutes do
          m_customers = m_customers + grumpy_i
          {i + 1, m_customers, m_customers}
        else
          save = save + grumpy_i - Enum.at(grumpy, i - minutes)
          if save > m_customers do
            {i + 1, save, save}
          else
            {i + 1, save, m_customers}
          end
        end
      end)
    total + m_customers
  end

  # Time Limit Exceeded 75/78
  @spec max_satisfied2(customers :: [integer], grumpy :: [integer], minutes :: integer) :: integer
  def max_satisfied2(customers, grumpy, minutes) do
    n = Enum.count(customers)
    {_, total, grumpy} =
      Enum.reduce(customers, {0, 0, grumpy}, fn customers_i, {i, total, grumpy} ->
        grumpy_i = Enum.at(grumpy, i)
        {i + 1, total + customers_i*(1 - grumpy_i), List.replace_at(grumpy, i, customers_i*grumpy_i)}
      end)
    {_, m_customers} =
      Enum.reduce_while(grumpy, {0, 0}, fn grumpy_i, {i, m_customers} ->
        if i < minutes do
          {:cont, {i + 1, m_customers + grumpy_i}}
        else
          {:halt, {i + 1, m_customers}}
        end
      end)
    if minutes < n do
      {_, m_customers} =
        Enum.reduce(minutes..n-1, {m_customers, m_customers}, fn i, {save, m_customers} ->
          save = save + Enum.at(grumpy, i) - Enum.at(grumpy, i - minutes)
          if save > m_customers do
            {save, save}
          else
            {save, m_customers}
          end
        end)
      total + m_customers
    else
      total + m_customers
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    customers = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    grumpy = for num <- String.split(Enum.at(flds, 1), ","), do: num |> String.trim() |> String.to_integer()
    minutes = Enum.at(flds, 2) |> String.to_integer()
    "customers = [" <>  Mylib.intList_to_string(customers) <> "], grumpy = [" <> Mylib.intList_to_string(grumpy) <> "], minutes = " <> Integer.to_string(minutes) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_satisfied(customers, grumpy, minutes)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
