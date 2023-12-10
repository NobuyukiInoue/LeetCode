defmodule Solution2 do
  # 544ms - 754ms
  defp start(nums) do
    Agent.start_link(fn -> nums end, name: __MODULE__)
  end

  defp restart(nums) do
    Agent.stop(__MODULE__)
    start(nums)
  end

  @spec init_(nums :: [integer]) :: any
  def init_(nums) do
    case start(nums) do
      {:ok, _} -> nil
      {:error, {:already_started, _}} -> restart(nums)
    end
  end

  @spec reset() :: [integer]
  def reset() do
    Agent.get(__MODULE__, & &1)
  end

  @spec shuffle() :: [integer]
  def shuffle() do
    Enum.shuffle(Agent.get(__MODULE__, & &1))
  end
end

# Your functions will be called as such:
# Solution.init_(nums)
# param_1 = Solution.reset()
# param_2 = Solution.shuffle()

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
