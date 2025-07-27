function Footer(){
    return(
        <>
            <footer class="bg-gray-800 text-white py-6">
                <div class="container mx-auto px-4 text-center">
                    <p>&copy; 2025 ThalPredict. All rights reserved.</p>
                    <div class="mt-4 space-x-4">
                        <a href="/privacy" class="text-gray-400 hover:text-white transition duration-300">Privacy Policy</a>
                        <a href="/terms" class="text-gray-400 hover:text-white transition duration-300">Terms of Service</a>
                        <a href="/contact" class="text-gray-400 hover:text-white transition duration-300">Contact Us</a>
                    </div>
                </div>
            </footer>
        </>
    )
}
export default Footer