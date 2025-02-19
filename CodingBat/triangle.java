package CodingBat;

public class triangle {
    public int triangle(int rows) {
        if (rows  <= 1) {
          return rows;
        }
        return rows + triangle(rows - 1);
      }      
}
