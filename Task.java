import java.util.*;

public class Task {
    public static void main(String[] args) {
        ArrayList<String> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();
        ArrayList<String> list3 = new ArrayList<>();
        ArrayList<Integer> players = new ArrayList<>();
        ArrayList<String> cards = new ArrayList<>();

        Collections.addAll(list1, "R", "G", "B", "W");

        for (int i = 1; i < 11; i++) {
            list2.add(i);
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 10; j++) {
                list3.add(list1.get(i) + list2.get(j));
            }
        }

        System.out.println("Input \"start N C\" to dispensing N random cards, to C players");
        Scanner scanner = new Scanner(System.in);

        int c = 0;
        int n = 0;

        while (true) {
            String order1 = scanner.nextLine();
            String[] words1 = order1.split(" ");
            n = Integer.parseInt(words1[1]);
            c = Integer.parseInt(words1[2]);

            if(!words1[0].equals("start")){
                System.out.println("Attention! command \"start\" input wrong . Input command again.");
            }
            else if (n * c > 40) {
                System.out.println("Attention! Only 40 cards almost. Dispensing cards again.");
            } else {
                break;
            }
        }

        String answer = "y";
        while (!answer.equals("n")) {

            System.out.println("Input \"get-cards C\" to dispensing cards to player, where C - players number.");

            int c_number = 0;
            while (true) {
                String order2 = scanner.nextLine();
                String[] words2 = order2.split(" ");
                c_number = Integer.parseInt(words2[1]);

                if (!words2[0].equals("get-cards")) {
                    System.out.println("Attention! command \"get-cards\" input wrong. Input command again.");
                } else if (c_number > c) {
                    System.out.println("Attention! Player's number more, than total players amount. Input command again.");
                } else if (players.contains(c_number)) {
                    System.out.println("This player already got cards. Input command again.");
                } else {
                    players.add(c_number);
                    break;
                }
            }

            cards.clear();
            for (int i = 0; i < n; i++) {
                cards.add(list3.get((int) (Math.random() * list3.size())));
                list3.remove(cards.get(i));
            }
            cards.add(0, Integer.toString(c_number));

            for (String x : cards) {
                System.out.print(x + " ");
            }
            System.out.println();

            if (list3.size() < n){
                System.out.println("No cards in pack.");
                break;
            }

            System.out.println("Play again? (y = yes, n = no):  ");
            answer = scanner.nextLine();

        }

        System.out.println();
        System.out.println("Cards were dispense.");
        System.out.println("Cards in pack left: " + String.join(", ", list3));
        System.out.println("Amount left cards in pack: " + list3.size());
    }
}
