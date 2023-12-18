class Solution {

    Queue<Integer> rq = new LinkedList<Integer>();
    Queue<Integer> dq = new LinkedList<Integer>();

    public String predictPartyVictory(String senate) {
        for(int i = 0; i < senate.length(); i++) {
            if(senate.charAt(i)== 'R') {
                rq.offer(i);
            } else {
                dq.offer(i);
            }
        }

        while(!dq.isEmpty() && !rq.isEmpty()) {
            if(rq.peek() < dq.peek()) {
                int i = rq.poll();
                dq.poll();
                rq.offer(i + senate.length());
            } else {
                int i = dq.poll();
                rq.poll();
                dq.offer(i + senate.length());
            }
        }

        if(rq.isEmpty()) {
            return "Dire";
        }
        return "Radiant";
    }
}