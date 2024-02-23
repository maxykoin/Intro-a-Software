public class main(){
    public static class mais(String[] arg){
        firstMovie = new movie();
        firstMovie.name = "Tangled";
        firstMovie.release = 2010;
        firstMovie.runtime = 100;

        firstMovie.ratings(5);
        firstMovie.ratings(3);
        firstMovie.ratings(4);

        System.out.println(firstMovie.name);
        System.out.println(sumRatings);
        System.out.println(allRatings);
    }
}

private class movie{
    String name;
    int release;
    int runtime;
    String director;
    double allRantings;
    int sumRatings;
    
    void ratings(grade){
        sumRatings += grade
        allRatings++
    }

    double meanRatings(){
        return sumRatings / allRantings
    }
}