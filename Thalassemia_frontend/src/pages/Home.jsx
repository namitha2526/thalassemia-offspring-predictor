import { Link } from "react-router-dom"
import NavBar from "../components/Navbar"
import Footer from "../components/Footer"

function Home(){
    return(
        <>
            <NavBar/>
            {/* <!-- Hero Section --> */}
            <section class="bg-blue-50 py-20 text-center">
                <div class="container mx-auto px-4">
                    <h1 class="text-5xl font-bold text-gray-800 mb-4 fade-in">Welcome to ThalPredict</h1>
                    <p class="text-xl text-gray-600 mb-8 fade-in">Predict Thalassemia risk for your child with advanced machine learning. Simple, fast, and reliable.</p>
                </div>
            </section>

                    {/* <!-- Features Section --> */}
            <section class="py-16 bg-white">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-semibold text-center text-gray-800 mb-12">Why Choose ThalPredict?</h2>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                        {/* <!-- Feature 1 --> */}
                        <div class="text-center p-6 bg-gray-50 rounded-lg shadow-md hover:shadow-lg transition duration-300">
                            <i class="fas fa-user-md text-4xl text-blue-600 mb-4"></i>
                            <h3 class="text-xl font-medium text-gray-800 mb-2">For Parents & Families</h3>
                            <p class="text-gray-600">Easily input parental data to assess Thalassemia risk for your child. Download detailed prediction reports in PDF.</p>
                        </div>
                        {/* <!-- Feature 2 --> */}
                        <div class="text-center p-6 bg-gray-50 rounded-lg shadow-md hover:shadow-lg transition duration-300">
                            <i class="fas fa-stethoscope text-4xl text-blue-600 mb-4"></i>
                            <h3 class="text-xl font-medium text-gray-800 mb-2">For Doctors</h3>
                            <p class="text-gray-600">Access advanced insights like feature importance to understand key factors influencing predictions.</p>
                        </div>
                        {/* <!-- Feature 3 --> */}
                        <div class="text-center p-6 bg-gray-50 rounded-lg shadow-md hover:shadow-lg transition duration-300">
                            <i class="fas fa-code text-4xl text-blue-600 mb-4"></i>
                            <h3 class="text-xl font-medium text-gray-800 mb-2">For Developers</h3>
                            <p class="text-gray-600">Integrate ThalPredict's API into your applications for seamless Thalassemia risk prediction.</p>
                        </div>
                    </div>
                </div>
            </section>

            {/* <!-- Call to Action Section --> */}
            <section class="bg-blue-600 text-white py-12 text-center">
                <div class="container mx-auto px-4">
                    <h2 class="text-3xl font-semibold mb-4">Ready to Predict Thalassemia Risk?</h2>
                    <p class="text-lg mb-6">Join thousands of users and healthcare professionals using ThalPredict to make informed decisions.</p>
                    <Link to="/user" className="bg-white text-blue-600 px-6 py-3 rounded-md hover:bg-gray-200 transition duration-300">Start Predicting Now</Link>
                </div>
            </section>

            <Footer/>
        </>
    )
}

export default Home