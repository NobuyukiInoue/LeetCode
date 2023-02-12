defmodule Solution do
  # 315ms - 402ms
  defmodule Heap do
    @leaf nil
    def new(), do: @leaf

    defp rank(@leaf), do: 0
    defp rank({r, _, _, _}), do: r

    defp merge(@leaf, t), do: t
    defp merge(t, @leaf), do: t

    defp merge({_, lv, ll, lr} = t1, {_, rv, rl, rr} = t2) do
      if lv >= rv do
        swipe(lv, ll, merge(lr, t2))
      else
        swipe(rv, rl, merge(t1, rr))
      end
    end

    defp swipe(v, left, right) do
      if rank(left) >= rank(right) do
        {rank(right) + 1, v, left, right}
      else
        {rank(left) + 1, v, right, left}
      end
    end

    def push(q, v) do
      merge(q, {1, v, @leaf, @leaf})
    end

    def pop(@leaf), do: nil
    def pop({_, v, @leaf, @leaf}), do: {v, @leaf}
    def pop({_, v, l, r}), do: {v, merge(l, r)}

    def reduce(@leaf, acc, _fun), do: acc

    def reduce(hp, acc, fun) do
      case pop(hp) do
        {nil, _} -> acc
        {top, hp} -> reduce(hp, fun.(top, acc), fun)
      end
    end
  end

  @spec pick_gifts(gifts :: [integer], k :: integer) :: integer
  def pick_gifts(gifts, k) do
    gifts
    |> Enum.reduce(Heap.new(), &Heap.push(&2, &1))
    |> aux(k)
  end

  def aux(hp, 0) do
    Heap.reduce(hp, 0, &+/2)
  end

  def aux(hp, k) do
    {n, hp} = Heap.pop(hp)

    hp
    |> Heap.push(n |> :math.sqrt() |> floor())
    |> aux(k - 1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    gifts = for num <- String.split(Enum.at(flds, 0), ","), do: num |> String.trim() |> String.to_integer()
    k = Enum.at(flds, 1) |> String.to_integer()
    "gifts = [" <>  Mylib.intList_to_string(gifts) <> "], k = " <> Integer.to_string(k) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.pick_gifts(gifts, k)
      "result = " <> Integer.to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
