import { Link } from "react-router-dom";

function NavBar(){

    return(
        <>
            <nav class="bg-blue-600 text-white py-4 shadow-md">
                <div class="container mx-auto px-4 flex justify-between items-center">
                    {/* <!-- Logo/Brand --> */}
                    <a href="/" class="text-2xl font-bold">ThalPredict</a>
                    {/* <!-- Navbar Buttons --> */}
                    <div class="space-x-4">
                        <Link to="/developers" className="bg-blue-700 hover:bg-blue-800 text-white px-4 py-2 rounded-md transition duration-300">Developers</Link>
                    </div>
                </div>
            </nav>
        </>
    )
}

export default NavBar