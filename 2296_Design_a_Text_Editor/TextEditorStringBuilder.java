import java.util.Stack;

class TextEditorStringBuilder {

    Stack<Character> ls;
    Stack<Character> rs;

    char curr;

    public TextEditor() {
        ls = new Stack<Character>();
        rs = new Stack<Character>();
    }
    
    public void addText(String text) {
        for(int i = 0; i < text.length(); i++) {
            ls.add(text.charAt(i));
        }
    }
    
    public int deleteText(int k) {
        int i = 0;

        while(i<k && !ls.isEmpty()) {
            Character temp = ls.pop();
            i++;
        }

        return i;
    }
    
    public String cursorLeft(int k) {
        int i = 0;

        String ans = "";

        while(i<k && !ls.isEmpty()) {
            rs.add(ls.pop());
            i++;
        }

        i = 0;
        while(i < 10 && !ls.isEmpty()) {
            Character temp = ls.pop();
            ans += temp;
            i++;
        }

        ans = new StringBuilder(ans).reverse().toString();

        if(ans != "") {
            for(i = 0; i < ans.length(); i++) {
                ls.add(ans.charAt(i));
            }
        }

        return ans;
    }
    
    public String cursorRight(int k) {
        int i = 0;

        String ans = "";

        while(i<k && !rs.isEmpty()) {
            ls.add(rs.pop());
            i++;
        }

        i = 0;
        while(i < 10 && !ls.isEmpty()) {
            Character temp = ls.pop();
            ans += temp;
            i++;
        }
        ans = new StringBuilder(ans).reverse().toString();


        if(ans != "") {
            for(i = 0; i < ans.length(); i++) {
                ls.add(ans.charAt(i));
            }
        }

        return ans;
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.addText(text);
 * int param_2 = obj.deleteText(k);
 * String param_3 = obj.cursorLeft(k);
 * String param_4 = obj.cursorRight(k);
 */