public class Biodata {
    String name;
    int age;
    String branch;

    public Biodata(String n, int a, String b){
        name = n;
        age = a;
        branch = b;
    }

    public void disaplay(){
        System.out.println("Name : " + name);
        System.out.println("Age : " + age);
        System.out.println("Branch : " + branch);
    }

    public static void main(String[] args) {
        Biodata A = new Biodata("SOUMYA", 19, "CSE");
        Biodata B = new Biodata("SATYA", 20, "CIVIL");

        A.disaplay();
        B.disaplay();
    }




}
