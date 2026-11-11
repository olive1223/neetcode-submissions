class PrefixTree {

    class Node {
        public boolean endOfWord;
        public HashMap<Character, Node> nextNodes;
        public Node(boolean endOfWord) {
            this.endOfWord = endOfWord;
            this.nextNodes = new HashMap<>();
        }
    }  
    private Node root;

    public PrefixTree() {
        this.root = new Node(false);
    }
    
    public void insert(String word) {
        Node curr = this.root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            boolean endOfWord = i == word.length() - 1;
            if (!curr.nextNodes.containsKey(c)) {
                curr.nextNodes.put(c, new Node(endOfWord));
            }
            curr = curr.nextNodes.get(c);
        }
        curr.endOfWord = true;
        return;
    }
    
    public boolean search(String word) {
        Node curr = this.root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            boolean endOfWord = i == word.length() - 1;
            Node next = curr.nextNodes.get(c);
            if (next == null) {
               return false;
            }
            curr = next;
        }
        return curr.endOfWord;
    }
    
    public boolean startsWith(String prefix) {
        Node curr = this.root;
        for (char c: prefix.toCharArray()) {
            Node next = curr.nextNodes.get(c);
            if (next == null) {
                return false;
            }
            curr = next;
        }
        return true;
    }
}