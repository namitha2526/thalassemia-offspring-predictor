import UserForm from '../components/UserForm';
import NavBar from '../components/Navbar';
import Footer from "../components/Footer"

function User(){
    return(
        <>
            <NavBar/>
            <div>
                <h1 className="heading">Fill the details to predict Thalassemia</h1>
                <UserForm/>
            </div>
            <Footer/>
        </>
    )
}

export default User