defmodule Solution do
  # 385ms - 392ms
  @spec decode(encoded :: [integer]) :: [integer]
  def decode(encoded) do
    n = Enum.count(encoded) + 1
    {i, a} =
      Enum.reduce(encoded, {0, 0}, fn encode, {i, a} ->
        a = Bitwise.bxor(a, i)
        if i < n and rem(i, 2) == 1 do
          {i + 1, Bitwise.bxor(a, encode)}
        else
          {i + 1, a}
        end
      end)
    a = Enum.reduce(i..n, a, fn i, a -> Bitwise.bxor(a, i) end)
    Enum.reduce_while(encoded, {0, [a], a}, fn enc, {i, res, tail} ->
      if i >= n - 2 do
        {:halt, {i, [tail | res], tail}}
      else
        tail = Bitwise.bxor(tail, enc)
        {:cont, {i, [tail | res], tail}}
        end
    end) |> elem(1) |> Enum.reverse
  end

  # Time Limit Exceeded. 54/63
  @spec decode1(encoded :: [integer]) :: [integer]
  def decode1(encoded) do
    n = Enum.count(encoded) + 1
    a =
      Enum.reduce(0..n, 0, fn i, a ->
        a = Bitwise.bxor(a, i)
        if i < n and rem(i, 2) == 1, do: Bitwise.bxor(a, Enum.at(encoded, i)), else: a
      end)
    Enum.reduce(0..n-2, {[a], a}, fn i, {res, tail} ->
      tail = Bitwise.bxor(tail, Enum.at(encoded, i))
      {[tail | res], tail}
    end) |> elem(0) |> Enum.reverse
  end

  # Time Limit Exceeded. 54/63
  @spec decode2(encoded :: [integer]) :: [integer]
  def decode2(encoded) do
    n = Enum.count(encoded) + 1
    a =
      Enum.reduce(0..n, 0, fn i, a ->
        a = Bitwise.bxor(a, i)
        if i < n and rem(i, 2) == 1, do: Bitwise.bxor(a, Enum.at(encoded, i)), else: a
      end)
    Enum.reduce(0..n-2, {[a], a}, fn i, {res, tail} ->
      tail = Bitwise.bxor(tail, Enum.at(encoded, i))
      {res ++ [tail], tail}
    end) |> elem(0)
  end

  # Time Limit Exceeded. 55/63
  @spec decode3(encoded :: [integer]) :: [integer]
  def decode3(encoded) do
    n = Enum.count(encoded) + 1
    a =
      Enum.reduce(0..n, 0, fn i, a ->
        a = Bitwise.bxor(a, i)
        if i < n and rem(i, 2) == 1, do: Bitwise.bxor(a, Enum.at(encoded, i)), else: a
      end)
    Enum.reduce_while(encoded, {0, [a], a}, fn enc, {i, res, tail} ->
      if i >= n - 2 do
        {:halt, {i, [tail | res], tail}}
      else
        tail = Bitwise.bxor(tail, enc)
        {:cont, {i, [tail | res], tail}}
        end
    end) |> elem(1) |> Enum.reverse
  end

  # Time Limit Exceeded. 54/63
  @spec decode4(encoded :: [integer]) :: [integer]
  def decode4(encoded) do
    n = Enum.count(encoded) + 1
    a =
      Enum.reduce(0..n, 0, fn i, a ->
        a = Bitwise.bxor(a, i)
        if i < n and rem(i, 2) == 1, do: Bitwise.bxor(a, Enum.at(encoded, i)), else: a
      end)
    Enum.reduce_while(encoded, {0, [a], a}, fn enc, {i, res, tail} ->
      if i >= n - 2 do
        {:halt, {i, res ++ [tail], tail}}
      else
        tail = Bitwise.bxor(tail, enc)
        {:cont, {i, res ++ [tail], tail}}
        end
    end) |> elem(1)
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    flds = String.replace(temp, ", ", ",")

    encoded = for n <- String.split(flds, ",") do String.to_integer(n) end
    "encoded = [" <> Mylib.intList_to_string(encoded) <> "]" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.decode(encoded)
      "result = [" <> Mylib.intList_to_string(result) <> "]" |> IO.puts
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
