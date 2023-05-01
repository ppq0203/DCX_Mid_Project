package jsp.member.model;



// 데이터의 전달을 담당하는 클래스 - DTO
public class MemberBean 
{
	private String id;			// 아이디
	private String pw; 	// 비밀번호
	private String phone;		// 전화
	private String address;		// 주소
	private String email;
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		this.pw = pw;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	@Override
	public String toString() {
		return "MemberBean [id=" + id + ", pw=" + pw + ", phone=" + phone + ", address=" + address + ", email=" + email
				+ "]";
	}
	
	
	
	}
	

