using Microsoft.AspNetCore.Mvc;

namespace WorldService.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WorldController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            return Ok("world");
        }
    }
}
