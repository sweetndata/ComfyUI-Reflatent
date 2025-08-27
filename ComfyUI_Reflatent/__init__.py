
class RefLatent:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"conditioning": ("CONDITIONING", ),
                            },
                "optional": {"latent": ("LATENT", ),}
               }

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "append"

    CATEGORY = "advanced/conditioning/edit_models"
    DESCRIPTION = "This node sets the guiding latent for an edit model. If the model supports it you can chain multiple to set multiple reference images."

    def append(self, conditioning, latent=None):
        if latent is not None:
            conditioning = self.conditioning_set_values(conditioning, {"reference_latents": [latent["samples"]]}, append=True)
        return (conditioning, )

    def conditioning_set_values(self, conditioning, values={}, append=False):
        c = []
        for t in conditioning:
            n = [t[0], t[1].copy()]
            for k in values:
                val = values[k]
                if append:
                    old_val = n[1].get(k, None)
                    if old_val is not None:
                        val = old_val + val

                n[1][k] = val
            c.append(n)

        return c


NODE_CLASS_MAPPINGS = {
    "RefLatent": RefLatent,
}