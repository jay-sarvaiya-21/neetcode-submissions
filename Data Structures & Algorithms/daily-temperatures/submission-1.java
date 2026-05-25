

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<>();
        int[] res = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            int currentTemp = temperatures[i];

            while (!stack.isEmpty() && currentTemp > stack.peek()[1]) {
                int index = stack.pop()[0];
                res[index] = i - index;
            }

            stack.push(new int[]{i, currentTemp});
        }

        return res;
    }
}
