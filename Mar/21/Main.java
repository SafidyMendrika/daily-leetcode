import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String[] recipes = {"bread"};
        List<List<String>> ingredients = new ArrayList<>();
        ingredients.add(Arrays.asList("yeast", "flour"));
        String[] supplies = {"yeast", "flour", "corn"};
        
        List<String> result = solution.findAllRecipes(recipes, ingredients, supplies);
        System.out.println(result);
    }
}
