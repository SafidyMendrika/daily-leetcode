import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        List<String> result = new ArrayList<>();
        
        Set<String> availableSupplies = new HashSet<>(Arrays.asList(supplies));
        
        Map<String, List<String>> recipeToIngredients = new HashMap<>();
        Set<String> recipeSet = new HashSet<>(Arrays.asList(recipes));
        
        for (int i = 0; i < recipes.length; i++) {
            recipeToIngredients.put(recipes[i], ingredients.get(i));
        }
        
        Set<String> visited = new HashSet<>();
        Set<String> preparing = new HashSet<>();
        
        for (String recipe : recipes) {
            if (canCreate(recipe, recipeToIngredients, availableSupplies, recipeSet, visited, preparing)) {
                result.add(recipe);
            }
        }
        
        return result;
    }
    
    private boolean canCreate(String recipe, 
                             Map<String, List<String>> recipeToIngredients, 
                             Set<String> supplies, 
                             Set<String> recipeSet,
                             Set<String> visited,
                             Set<String> preparing) {
        
        if (visited.contains(recipe)) {
            return supplies.contains(recipe);
        }
        
        if (preparing.contains(recipe)) {
            return false;
        }
        
        if (!recipeSet.contains(recipe)) {
            return supplies.contains(recipe);
        }
        
        preparing.add(recipe);
        
        for (String ingredient : recipeToIngredients.get(recipe)) {
            if (!supplies.contains(ingredient) && 
                !canCreate(ingredient, recipeToIngredients, supplies, recipeSet, visited, preparing)) {
                preparing.remove(recipe);
                visited.add(recipe);
                return false;
            }
        }
        
        supplies.add(recipe);
        
        visited.add(recipe);
        preparing.remove(recipe);
        
        return true;
    }
}