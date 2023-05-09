const loginBoxProfessor = document.getElementById("login-box-professor");
const loginBoxStudent = document.getElementById("login-box-student");
const showLoginProfessorButton = document.getElementById(
  "show-login-professor"
);
const showLoginStudentButton = document.getElementById("show-login-student");

// Show professor login box when "Professor" button is clicked
showLoginProfessorButton.addEventListener("click", () => {
  loginBoxProfessor.style.right = "0";
  loginBoxStudent.style.right = "-500px";
});

// Show student login box when "Student" button is clicked
showLoginStudentButton.addEventListener("click", () => {
  loginBoxStudent.style.right = "0";
  loginBoxProfessor.style.right = "-500px";
});

// Close login box when user clicks outside of it
document.addEventListener("click", (event) => {
  const isClickInsideProfessorBox = loginBoxProfessor.contains(event.target);
  const isClickInsideStudentBox = loginBoxStudent.contains(event.target);
  const isClickOnProfessorButton = event.target === showLoginProfessorButton;
  const isClickOnStudentButton = event.target === showLoginStudentButton;

  if (
    !isClickInsideProfessorBox &&
    !isClickOnProfessorButton &&
    loginBoxProfessor.style.right === "0px"
  ) {
    loginBoxProfessor.style.right = "-500px";
  }

  if (
    !isClickInsideStudentBox &&
    !isClickOnStudentButton &&
    loginBoxStudent.style.right === "0px"
  ) {
    loginBoxStudent.style.right = "-500px";
  }
});
