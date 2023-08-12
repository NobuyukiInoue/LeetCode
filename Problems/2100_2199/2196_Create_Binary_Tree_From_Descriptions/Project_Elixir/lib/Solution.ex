defmodule Solution do
  # 673ms - 681ms
  @spec create_binary_tree(descriptions :: [[integer]]) :: TreeNode.t | nil
  def create_binary_tree(descriptions) do
    {root, map} = find_root(descriptions)
    build_tree(root, map)
  end

  def find_root(descriptions) do
    {ps, cs, map} =
      descriptions
      |> Enum.reduce({MapSet.new(), MapSet.new(), %{}}, fn [p, c, is_left], {ps, cs, acc} ->
        {MapSet.put(ps, p), MapSet.put(cs, c),
         Map.update(acc, p, %{is_left => c}, fn v -> Map.put(v, is_left, c) end)}
      end)

    {MapSet.difference(ps, cs) |> MapSet.to_list() |> hd(), map}
  end

  def build_tree(nil, _map), do: nil

  def build_tree(val, map) do
    c = Map.get(map, val)

    if c == nil do
      %TreeNode{val: val}
    else
      l = build_tree(Map.get(c, 1), map)
      r = build_tree(Map.get(c, 0), map)
      %TreeNode{val: val, left: l, right: r}
    end
  end

  @spec loop_main(temp :: String.t) :: :ok
  def loop_main(temp) do
    temp = String.replace(temp, "[[", "")
    temp = String.replace(temp, "]]", "")
    temp = String.replace(temp, ", ", ",")
    flds = String.split(temp, "],[")

    descriptions =
    for fld <- flds do
      for n <- String.split(fld, ",") do
        String.to_integer(n)
      end
    end

    Mylib.matrix_to_string("descriptions", descriptions) |> IO.puts()

    exectime = Benchmark.measure(fn ->
      result = Solution.create_binary_tree(descriptions)
      "result = " <> OperateTreeNode.treenode_to_string(result) |> IO.puts()
    end)

    "Execute time : " <> Float.to_string(Float.round(exectime, 3)) <> " [s]\n" |> IO.puts()
  end
end
