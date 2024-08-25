defmodule Solution do
  # 730ms - 819ms
  @spec max_turbulence_size(arr :: [integer]) :: integer
  def max_turbulence_size(arr) do
    {n, m_arr} = Enum.reduce(arr, {0, %{}}, fn num, {i, m_arr} ->
      {i + 1, Map.put(m_arr, i, num)}
    end)
    Enum.reduce(0..n-1, {0, 0}, fn i, {ans, clen} ->
      clen =
        cond do
          i >= 2 and ((m_arr[i-2] > m_arr[i-1] and m_arr[i-1] < m_arr[i]) or (m_arr[i-2] < m_arr[i-1] and m_arr[i-1] > m_arr[i])) ->
            clen + 1
          i >= 1 and m_arr[i-1] != m_arr[i] ->
            2
          true ->
            1
        end
		  {max(ans, clen), clen}
    end) |> elem(0)
  end

  # Time Limite Exceeded. (79/93)
  @spec max_turbulence_size2(arr :: [integer]) :: integer
  def max_turbulence_size2(arr) do
    n = Enum.count(arr)
    Enum.reduce(0..n-1, {0, 0}, fn i, {ans, clen} ->
      clen =
        cond do
          i >= 2 and ((Enum.at(arr, i-2) > Enum.at(arr, i-1) and Enum.at(arr, i-1) < Enum.at(arr, i)) or (Enum.at(arr, i-2) < Enum.at(arr, i-1) and Enum.at(arr, i-1) > Enum.at(arr, i))) ->
            clen + 1
          i >= 1 and Enum.at(arr, i-1) != Enum.at(arr, i) ->
            2
          true ->
            1
        end
		  {max(ans, clen), clen}
    end) |> elem(0)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    arrs = for n <- String.split(flds, ",") do String.to_integer(n) end
    "arrs = [" <> Mylib.intList_to_string(arrs) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.max_turbulence_size(arrs)
      "result = " <> Integer.to_string(result) |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
