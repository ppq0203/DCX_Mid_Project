package jsp.Recipe;

public class Ingredient {
	
	private String id;
	private String i_name;
	private int i_quantity;
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getI_name() {
		return i_name;
	}
	public void setI_name(String i_name) {
		this.i_name = i_name;
	}
	public int getI_quantity() {
		return i_quantity;
	}
	public void setI_quantity(int i_quantity) {
		this.i_quantity = i_quantity;
	}
	@Override
	public String toString() {
		return "Ingredient [id=" + id + ", i_name=" + i_name + ", i_quantity=" + i_quantity + "]";
	}
	
}
