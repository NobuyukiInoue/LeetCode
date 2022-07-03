defmodule Solution do
  import Integer

  @spec longest_palindrome(s :: String.t) :: String.t
  def longest_palindrome(s) do
    if String.length(s) < 2 do
      s
    else
      chars =
        s
        |> String.graphemes()
        |> Enum.intersperse(" ")
        |> List.to_tuple()

      {center, radius} = max_palindrome_circle(chars)

      for i <- (center - radius)..(center + radius),
          char = elem(chars, i),
          char != " ",
          into: "",
      do: char
    end
  end

  defp max_palindrome_circle(chars) do
    len = tuple_size(chars)
    for center <- 0..tuple_size(chars)-1, reduce: {0, 0} do
      {_, max_radius} = acc ->
        radius = Stream.unfold(0, fn
          radius when radius > center ->
            nil

          radius when radius > len - center - 1 ->
            nil

          radius when elem(chars, center - radius) != elem(chars, center + radius) ->
            nil

          radius ->
            {radius, radius + 1}
        end)
        |> Enum.at(-1)

      case {center, radius} do
        {_, r} when r > max_radius -> {center, radius}
        {_, 0} -> acc
        {_, ^max_radius} when is_odd(center) -> {center, radius}
        _ -> acc
      end
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[", "")
    temp = String.replace(temp, "]", "")
    s = String.replace(temp, "\"", "")
    "s = \"" <> s <> "\"" |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.longest_palindrome(s)
      "result = \"" <> result <> "\"" |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
