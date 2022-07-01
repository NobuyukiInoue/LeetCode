defmodule Main do
  @moduledoc """
  Documentation for `Main`.
  """
  def hello() do
    "hello!" |> IO.puts()
  end

  def main(args \\ []) do
    if Enum.count(args) < 1 do
      "Usage) ./main <testdata.txt>" |> IO.puts()
      exit "1"
    end

    case File.open(args, [:read]) do
      {:ok, fp} ->
        # read one line.
        Enum.each(IO.stream(fp, :line), fn(line) ->
          temp = String.trim(line)
          if String.length(temp) > 0 do
            "args = " <> temp |> IO.puts()
            Solution.loop_main(temp)
          end
        end)
        File.close(fp)
      {:error, :enoent} -> "Cannot open " <> Enum.at(args, 0) |> IO.puts()
    end
  end
end
