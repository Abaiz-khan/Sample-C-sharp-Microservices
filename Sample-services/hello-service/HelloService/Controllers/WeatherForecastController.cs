using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;

namespace HelloService.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class HelloController : ControllerBase
    {
        private readonly ILogger<HelloController> _logger;
        private readonly IConfiguration _configuration;

        public HelloController(ILogger<HelloController> logger, IConfiguration configuration)
        {
            _logger = logger;
            _configuration = configuration;
        }

        [HttpGet]
        public IActionResult Get()
        {
            bool isHelloFeatureEnabled = _configuration.GetValue<bool>("FeatureFlags:HelloFeatureEnabled");

            _logger.LogInformation($"Hello feature enabled: {isHelloFeatureEnabled}");

            if (isHelloFeatureEnabled)
            {
                return Ok("Hello");
            }
            else
            {
                return NotFound(); // or any appropriate response for when the feature is disabled
            }
        }
    }
}