public class test {
    public static void main(String[] arg) {
        movie firstMovie = new movie();
        firstMovie.name = "Tangled";
        firstMovie.release = 2010;
        firstMovie.runtime = 100;

        firstMovie.ratings(5);
        firstMovie.ratings(3);
        firstMovie.ratings(4);

        System.out.println(firstMovie.name);
    }
}

private class movie {
    String name;
    int release;
    int runtime;
    String director;
    double allRatings;
    double sumRatings;
    double grade;

    double ratings(int grade) {
        sumRatings += grade;
        allRatings++;
    }

    double meanRatings() {
        return sumRatings / allRatings;
    }
}