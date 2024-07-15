class Solution {
    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

    public int minStoneSum(int[] piles, int k) {
        for(int i=0; i < piles.length; i++) {
            pq.add(piles[i]);
        }

        for(int i=0; i < k; i++) {
            int stone = pq.poll();

            if(stone % 2 == 0) {
                stone = stone / 2;
            } else {
                stone = (int)Math.floor((double)(stone/2) + 1);
            }

            pq.add(stone);
        }

        int stoneSum = 0;

        Iterator iterator = pq.iterator();
 
        while (iterator.hasNext()) {
            stoneSum = stoneSum + pq.poll();
        }


        return stoneSum;

    }
}