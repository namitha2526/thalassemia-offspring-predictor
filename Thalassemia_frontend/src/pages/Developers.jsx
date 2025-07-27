import NavBar from "../components/Navbar"
import Footer from "../components/Footer"

function Developers(){
    return(
        <>  
            <NavBar/>
            <section class="bg-white rounded-lg shadow-lg p-6 mb-8">
                <h2 class="text-2xl font-semibold mb-4 text-center">Meet the Team: TECH PHANTOMS</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div class="text-center transform transition duration-300 hover:scale-105">
                        <div class="bg-blue-100 p-4 rounded-lg">
                            <h3 class="text-lg font-medium text-blue-600">Namitha R</h3>
                            <p class="text-gray-700">Role: Data & Domain Specialist</p>
                            <p class="text-gray-700">Tasks: Data collection, cleaning, and medical research validation.</p>
                        </div>
                    </div>
                    <div class="text-center transform transition duration-300 hover:scale-105">
                        <div class="bg-blue-100 p-4 rounded-lg">
                            <h3 class="text-lg font-medium text-blue-600">Mourya Vardhan B K</h3>
                            <p class="text-gray-700">Role: Frontend Developer</p>
                            <p class="text-gray-700">Tasks: Interface design, and user flow planning</p>
                        </div>
                    </div>
                    <div class="text-center transform transition duration-300 hover:scale-105">
                        <div class="bg-blue-100 p-4 rounded-lg">
                            <h3 class="text-lg font-medium text-blue-600">Aman Nayan</h3>
                            <p class="text-gray-700">Role: ML & Backend Developer</p>
                            <p class="text-gray-700">Tasks: Model development, API integration, and backend logic</p>
                        </div>
                    </div>
                    <div class="text-center transform transition duration-300 hover:scale-105">
                        <div class="bg-blue-100 p-4 rounded-lg">
                            <h3 class="text-lg font-medium text-blue-600">Nayana D</h3>
                            <p class="text-gray-700">Role: Data Assistant</p>
                            <p class="text-gray-700">Tasks: Support in data preparation and formatting</p>
                        </div>
                    </div>
                </div>
            </section>

            {/* <!-- Project Stats --> */}
            <section class="bg-white rounded-lg shadow-lg p-6">
                <h2 class="text-2xl font-semibold mb-4 text-center">Project Stats</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
                    <div>
                        <h3 class="text-lg font-medium text-blue-600">Dataset Size</h3>
                        <p id="datasetCounter" class="text-2xl font-bold text-gray-700">200000</p>
                        <p class="text-gray-700">Rows</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-medium text-blue-600">Model Accuracy</h3>
                        <p id="accuracyCounter" class="text-2xl font-bold text-gray-700">92.01%</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-medium text-blue-600">Features Used</h3>
                        <p id="featuresCounter" class="text-2xl font-bold text-gray-700">8</p>
                    </div>
                </div>
            </section>
            <Footer/>
        </>
    )
}
export default Developers