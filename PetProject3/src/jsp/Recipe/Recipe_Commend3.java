package jsp.Recipe;

public class Recipe_Commend3 {

    public static void main(String[] args) {
    	//함수 호출을 위한 준비
    	IngredientDAO dao = new IngredientDAO();
    	
    	//INSERT(입력)
    	
    	//Ingredients_Img 1행 데이터 저장하기
//    	dao.insertImg("감자","#FFD966",6.3f,140.2f,"감자","https://naver.com/이미지/감자.jpg");
    			
    	//Ingredients_Price 1개 행 입력하기
//    	dao.insertPrice("감자", 2218);
    	
    	//Ingredients 새로운 데이타 1행 입력
//    	dao.insertIngredient("choi123", "대파", 15f, "g");
    	
    	//Recipe_Content 1개 행 입력하기
//		dao.insertContent("","","");
    	
    	//Recipe_Ingredients 1개 행 입력하기
//		dao.insertRIngredient("", "", f, "");
    	
    	//Recipe 1개 행 입력하기
//		dao.insertRecipe("126845", "어묵고추장찌개", "찌개","1인분", "초급",  "20분",10);
    	
    	
    	
    	//FILE(입력 및 저장)
    	
       	//Recipe_Contentcsv 파일로 전체 입력하기
//		dao.CSV_Recipe_Content("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\SNO_AND_ING.csv");
    	
    	//출력된 데이터 CSV 파일로 저장하기 
//		dao.saveToCsv1("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\test.csv");
		
    	//Recipe_Ingredients csv 파일로 전체 입력하기
//		 dao.CSV_Recipe_Ingredients("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\ING_BEFORE_Finish_4.csv");
    	
    	//Recipe csv 파일로 전체 입력하기
//		dao.CSV_Recipe("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\MAIN_RECIPE_TABLE.csv");
    	
    	
    	
    	
    	//SELECT(출력)
    	
    	//Ingredients_Price 재료명으로 가격 조회하기
//    	RecipeDTO result = dao.select_Price("감자");
//    	if (result != null){
//    	System.out.println("재료명: " + result.getING_NAME());
//    	System.out.println("가격: " + result.getI_price()+"원");		
//    					 	} 
    	
    	//Ingredients ID에 입력된 재료와 수량 조회
//		RecipeDTO result = i_dao.selectIngredient("id");
//		if (result != null) {
//			System.out.println("아이디: " + result.getId());
//			System.out.println("재료명: " + result.getING_NAME());
//			System.out.println("보유량: " + result.getING_AMOUNT() + result.getING_UNIT());
//							}
    	
    	//Recipe_Ingredients 레시피 넘버로 조회하기
    	RecipeDTO result = dao.selectRecipe_Ingredient("128671");
    	if (result != null){
    		System.out.println("레시피번호: " + result.getRCP_SNO());
    		System.out.println("레시피이름: " + result.getING_NAME());
    		System.out.println("보유량: " + result.getING_AMOUNT() + result.getING_UNIT());			
    			 			} 
    	
		//Recipe 레시피 넘버로 조회하기
//		RecipeDTO result = dao.selectRecipe("6258951");
//		 if (result != null){
//			System.out.println("레시피번호: " + result.getRCP_SNO());
//			System.out.println("요리명: " + result.getCKG_NM());
//			System.out.println("요리종류: " + result.getCKG_KND_ACTO_NM());
//			System.out.println("요리인분: " + result.getCKG_INBUN_NM());
//			System.out.println("요리난이도: " + result.getCKG_DODF_NM());
//			System.out.println("요리시간: " + result.getCKG_TIME_NM());
//			System.out.println("추천수: " + result.getRCMM_CNT());
//		 					}
    			
    	
    	
    	//UPDATE(수정)
    	
    	//ID와 재료명으로 데이터 수정
//    	dao.updatePrice("ING_NAME", i_price);
    	
    	//ID와 재료명으로 데이터 수정
//		i_dao.updateIngredient("dkqydhd", "양파");
    					
    	
    	
    	
    	//DELETE(삭제)
    	
    	//Ingredients ID와 재료명으로 데이터 삭제
//    	i_dao.deleteIngredient("asdfasf", "대파");		
    			
    										}
	
							  }
	